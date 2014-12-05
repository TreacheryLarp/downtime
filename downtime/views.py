from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from downtime.models import Session

class IndexView(generic.ListView):
    template_name = 'downtime/index.html'
    context_object_name = 'session_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Session.objects.all()

@login_required
def profile(request):
    return render(request, 'downtime/profile.html', {'character': request.user.character})

class SessionView(generic.DetailView):
    model = Session
    template_name = 'downtime/session.html'

@login_required
def session(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    return render(request, 'downtime/session.html', {'session': session})

@login_required
def submit(request):
    return HttpResponse('Submit your report here.')
