from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.formtools.wizard.views import SessionWizardView
from django.utils.decorators import method_decorator

from downtime.models import Session

@login_required
def profile(request):
    return render(request, 'downtime/profile.html', {'character': request.user.character,
                                                     'session_list': Session.objects.all()})

@login_required
def session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    character = request.user.character
    data =  {'session': session,
             'character': character,
             'has_submitted': session.has_submitted(character)}
    return render(request, 'downtime/session.html', data)

class SubmitWizard(SessionWizardView):
    template_name = 'downtime/submit_wizard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        session =  get_object_or_404(Session, pk=kwargs['pk'])
        character = self.request.user.character
        return super(SessionWizardView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self, step):
        return {'user': self.request.user}

    def done(self, form_list, **kwargs):
        session =  get_object_or_404(Session, pk=kwargs['pk'])
        character = self.request.user.character
        for f in form_list:
            f.fill_save(session, character)
        return HttpResponseRedirect('/s/%s' % kwargs['pk'])
