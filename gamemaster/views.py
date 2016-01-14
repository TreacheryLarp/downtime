from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.utils import timezone
from django.shortcuts import redirect

from players.models import *

def close(request):
    return render(request, 'closewindow.html')

def character(request, session, character):
    context = {
        'character': get_object_or_404(Character, id=character),
        'session':  get_object_or_404(Character, id=character),
        'actions': Action.objects.filter(character=character, session=session),
        'disciplines': Action.objects.filter(character=character, session=session),
        'feedings': Feeding.objects.filter(character=character, session=session),
    }
    return render(request, 'character.html', context)

def toggle_session(request, session):
    session_obj = get_object_or_404(Session, id=session)
    session_obj.is_open = not session_obj.is_open
    session_obj.save()
    return redirect('sessions')

class SessionListView(ListView):
    model = Session
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super(SessionListView, self).get_context_data(**kwargs)
        context['characters'] = Character.objects.all()
        context['type'] = 'sessions'
        context['sessions'] = self.object_list
        return context


class ActionListView(ListView):
    model = Action
    template_name = 'list.html'

    def get_queryset(self):
        self.session = get_object_or_404(Session, id=self.kwargs['session'])
        return Action.objects.filter(session=self.session)

    def get_context_data(self, **kwargs):
        context = super(ActionListView, self).get_context_data(**kwargs)
        session_name = get_object_or_404(Session, id=self.kwargs['session']).name
        context['session_name'] = session_name
        context['characters'] = Character.objects.all()
        context['action_types'] = ActionType.objects.all()
        context['type'] = 'actions'
        context['actions'] = self.object_list
        return context


class CharacterListView(ListView):
    model = Character
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super(CharacterListView, self).get_context_data(**kwargs)
        session = get_object_or_404(Session, id=self.kwargs['session'])
        context['session'] = session
        context['clans'] = Clan.objects.all()
        context['ages'] = Age.objects.all()
        context['type'] = 'characters'
        for c in self.object_list:
            c.has_submitted = c.submitted(session)
        context['characters'] = self.object_list
        return context


class DisciplineListView(ListView):
    model = ActiveDisciplines
    template_name = 'list.html'

    def get_queryset(self):
        self.session = get_object_or_404(Session, id=self.kwargs['session'])
        return ActiveDisciplines.objects.filter(session=self.session)

    def get_context_data(self, **kwargs):
        context = super(DisciplineListView, self).get_context_data(**kwargs)
        session_name = get_object_or_404(Session, id=self.kwargs['session']).name
        context['session_name'] = session_name
        context['type'] = 'disciplines'
        context['disciplines'] = self.object_list
        return context


class FeedingListView(ListView):
    model = Feeding
    template_name = 'list.html'

    def get_queryset(self):
        self.session = get_object_or_404(Session, id=self.kwargs['session'])
        return Feeding.objects.filter(session=self.session)

    def get_context_data(self, **kwargs):
        context = super(FeedingListView, self).get_context_data(**kwargs)
        session_name = get_object_or_404(Session, id=self.kwargs['session']).name
        context['session_name'] = session_name
        context['characters'] = Character.objects.all()
        context['domains'] = Domain.objects.all()
        context['type'] = 'feedings'
        context['feedings'] = self.object_list
        return context


class ActionUpdate(UpdateView):
    model = Action
    template_name = 'editor.html'
    fields = ['character', 'action_type', 'description', 'resolved']
    success_url = reverse_lazy('closewindow')

    def get_context_data(self, **kwargs):
        context = super(ActionUpdate, self).get_context_data(**kwargs)
        context['request'] = self.request
        session = self.object.session
        character = self.object.character
        adisc = ActiveDisciplines.objects.filter(session=session, character=character)
        if len(adisc) > 0:
            disc = adisc[0]
            context['extra_title'] = 'Active Disciplines'
            context['extra_data'] = ', '.join([d.name for d in disc.disciplines.all()])
        return context


class FeedingUpdate(UpdateView):
    model = Feeding
    template_name = 'editor.html'
    fields = ['character', 'domain', 'feeding_points', 'discipline', 'description', 'resolved']
    success_url = reverse_lazy('closewindow')

    def get_context_data(self, **kwargs):
        context = super(FeedingUpdate, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context


class CharUpdate(UpdateView):
    model = Character
    template_name = 'editor.html'
    success_url = reverse_lazy('closewindow')

    def get_context_data(self, **kwargs):
        context = super(CharUpdate, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context
