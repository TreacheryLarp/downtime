from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from downtime.models import Session

@login_required
def profile(request):
    return render(request, 'downtime/profile.html', {'character': request.user.character,
                                                     'session_list': Session.objects.all()})

@login_required
def session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    character = request.user.character
    active_disciplines = session.active_disciplines.filter(character=character)
    return render(request, 'downtime/session.html', {'session': session,
                                                     'character': character,
                                                     'active_disciplines': active_disciplines})
