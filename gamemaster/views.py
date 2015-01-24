from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.utils import timezone

from players.models import Session, Action, Character

class SessionListView(ListView):
    model = Session
    template_name = 'sessions.html'

    def get_context_data(self, **kwargs):
        context = super(SessionListView, self).get_context_data(**kwargs)
        context['characters'] = Character.objects.all()
        return context

class ActionListView(ListView):
    model = Action
    template_name = 'actions.html'

    def get_queryset(self):
        self.session = get_object_or_404(Session, id=self.kwargs['session'])
        return Action.objects.filter(session=self.session)
