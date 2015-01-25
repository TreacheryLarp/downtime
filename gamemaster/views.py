from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.utils import timezone

from players.models import Session, Action, Character, ActionType

def close(request):
    return render(request, 'closewindow.html')

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

    def get_context_data(self, **kwargs):
        context = super(ActionListView, self).get_context_data(**kwargs)
        context['characters'] = Character.objects.all()
        context['action_types'] = ActionType.objects.all()
        return context


class ActionUpdate(UpdateView):
    model = Action
    template_name = 'action.html'
    success_url = reverse_lazy('closewindow')
