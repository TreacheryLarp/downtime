from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.utils import timezone

from players.models import Session, Action, Character, ActionType, ActiveDisciplines

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
    template_name = 'editor.html'
    fields = ['action_type', 'character', 'description', 'resolved']
    success_url = reverse_lazy('closewindow')

    def get_context_data(self, **kwargs):
        context = super(ActionUpdate, self).get_context_data(**kwargs)
        session = self.object.session
        character = self.object.character
        adisc = ActiveDisciplines.objects.filter(session=session, character=character)
        if len(adisc) > 0:
            disc = adisc[0]
            context['extra_title'] = 'Active Disciplines'
            context['extra_data'] = ', '.join([d.name for d in disc.disciplines.all()])
        return context
