from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import models
from formtools.wizard.views import SessionWizardView
from django.utils.decorators import method_decorator
from django.forms.models import modelformset_factory
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from players import forms
from players.models import *


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
@user_passes_test(lambda u: not u.is_superuser, login_url='/gm/')
def profile(request):
    session_state = []
    for session in Session.objects.order_by('name').all():
        state = session.resolved_state(request.user.character)
        session_state.append({'state': state, 'session': session})

    return render(request, 'profile.html',
                  {'character': request.user.character,
                   'session_list': session_state})


@login_required
@user_passes_test(lambda u: not u.is_superuser, login_url='/gm/')
def session(request, session):
    session = get_object_or_404(Session, pk=session)
    character = request.user.character
    data = {'session': session,
            'character': character,
            'rumor_list': Rumor.objects.filter(session=session,
                                               recipients=character),
            'submitted': character.submitted(session),
            'extra_actions': ExtraAction.objects.filter(session=session,
                                                        character=character),
            'request': request}
    return render(request, 'session.html', data)


@login_required
@user_passes_test(lambda u: not u.is_superuser, login_url='/gm/')
def wizard(request, session):
    data = {
        'user': request.user,
        'character': request.user.character,
        'session': get_object_or_404(Session,
                                     pk=session)
    }
    initial = {'0': data, '1': data, '2': data, }

    if not data['session'].is_open:
        raise PermissionDenied('Session closed')

    Action.objects.filter(character=request.user.character,
                          session=session).delete()
    ActiveDisciplines.objects.filter(character=request.user.character,
                                     session=session).delete()
    Feeding.objects.filter(character=request.user.character,
                           session=session).delete()

    return SubmitWizard.as_view(
        [
            modelformset_factory(ActiveDisciplines,
                                 formset=forms.DisciplineActivationFormSet,
                                 fields=['disciplines']),
            modelformset_factory(Feeding,
                                 formset=forms.FeedingFormSet,
                                 fields=['domain', 'feeding_points',
                                         'discipline', 'description']),
            modelformset_factory(Action,
                                 formset=forms.ActionFormSet,
                                 fields=['action_type', 'description'])
        ],
        initial_dict=initial)(request, **data)


class SubmitWizard(SessionWizardView):
    template_name = 'submit_wizard.html'

    def done(self, form_list, **kwargs):
        for f in form_list:
            f.fill_save()
        return HttpResponseRedirect('/s/%s' % kwargs['session'].id)

    def get_context_data(self, form, **kwargs):
        context = super(SubmitWizard, self).get_context_data(form=form,
                                                             **kwargs)
        if self.steps.current == '0':
            context.update({'stepTitle': 'Active Disciplines'})
        elif self.steps.current == '1':
            context.update({'stepTitle': 'Feeding'})
        elif self.steps.current == '2':
            context.update({'stepTitle': 'Actions'})
            context.update({'help_texts': ActionType.help_texts()})
        return context
