from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.formtools.wizard.views import SessionWizardView
from django.utils.decorators import method_decorator
from django.forms.models import modelformset_factory

from downtime import forms
from downtime.models import Session, Action

@login_required
def profile(request):
    return render(request, 'downtime/profile.html', {'character': request.user.character,
                                                     'session_list': Session.objects.all()})

@login_required
def session(request, session):
    session = get_object_or_404(Session, pk=session)
    character = request.user.character
    data =  {'session': session,
             'character': character}
    return render(request, 'downtime/session.html', data)

@login_required
def wizard(request, session):
    data = {
        'user': request.user,
        'character': request.user.character,
        'session': session
    }
    initial = {
        '0': data,
        '1': data,
        '2': data,
    }
    return SubmitWizard.as_view([
        forms.DisciplineActivationForm,
        forms.FeedingForm,
        modelformset_factory(Action, formset=forms.ActionFormSet, fields=('action_type', 'description'))
        ], initial_dict=initial)(request, **data)


class SubmitWizard(SessionWizardView):
    template_name = 'downtime/submit_wizard.html'

    #def get_form_kwargs(self, step):
    #    return {'user': self.request.user,
    #            'session': self.session}

    def done(self, form_list, **kwargs):
        session =  get_object_or_404(Session, pk=kwargs['session'])
        character = self.request.user.character
        for f in form_list:
            f.fill_save(session, character)
        return HttpResponseRedirect('/s/%s' % kwargs['session'])
