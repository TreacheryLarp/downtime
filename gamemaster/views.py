from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from players.models import Session

class SessionListView(ListView):
    model = Session
    template_name = 'sessions.html'
