from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from downtime.models import Session

def index(request):
    context = {'session_list': Session.objects.all()}
    return render(request, 'downtime/index.html', context)

def session(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    return render(request, 'downtime/session.html', {'session': session})

def submit(request):
    return HttpResponse('Submit your report here.')
