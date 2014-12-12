from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.formtools.wizard.views import SessionWizardView

from downtime.models import Session

@login_required
def profile(request):
    return render(request, 'downtime/profile.html', {'character': request.user.character,
                                                     'session_list': Session.objects.all()})

@login_required
def session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    character = request.user.character
    active_disciplines = None
    if session.active_disciplines.filter(character=character).exists():
        active_disciplines = session.active_disciplines.get(character=character)
    data =  {'session': session,
             'character': character,
             'active_disciplines': active_disciplines}
    return render(request, 'downtime/session.html', data)

# login dectorator is in urlconf
class SubmitWizard(SessionWizardView):
    template_name = 'downtime/submit_wizard.html'

    def get_form_kwargs(self, step):
        return {'user': self.request.user}

    def done(self, form_list, **kwargs):
        session =  get_object_or_404(Session, pk=self.args[0])
        # do_something_with_the_form_data(form_list)
        print(form_list)
        return HttpResponseRedirect('/')
