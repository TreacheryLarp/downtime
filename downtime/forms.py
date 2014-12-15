from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.models import BaseModelFormSet

from downtime.models import *

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(LoginForm, self).confirm_login_allowed(user)
        if not user.character:
            raise forms.ValidationError(
                _('This user has no character.'),
                code='inactive',
            )


# Session submit forms
class SessionFormSet(BaseModelFormSet):

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial')
        self.user = initial['user']
        self.character = initial['character']
        self.session = initial['session']
        super(SessionFormSet, self).__init__(*args, **kwargs)

    def fill_save(self, session, character):
        instances = self.save(commit=False)
        for instance in instances:
            instance.session = session
            instance.character = character
            instance.save()
        self.save_m2m()
        for form in self.deleted_forms:
            if form.instance != None:
                form.instance.delete()


class DisciplineActivationFormSet(SessionFormSet):

    def __init__(self, *args, **kwargs):
        super(DisciplineActivationFormSet, self).__init__(*args, **kwargs)
        self.queryset = ActiveDisciplines.objects.filter(character=self.character, session=self.session)
        self.max_num = 1
        self.can_delete = True
        for form in self.forms:
            form.fields['disciplines'].queryset = self.user.character.disciplines.all()


class ActionFormSet(SessionFormSet):

    def __init__(self, *args, **kwargs):
        self.fields = ('action_type', 'description')
        super(ActionFormSet, self).__init__(*args, **kwargs)
        self.queryset = Action.objects.filter(character=self.character, session=self.session)
        self.extra = self.character.action_count()
        self.max_num = self.character.action_count()
        self.can_delete = True


class FeedingFormSet(SessionFormSet):

    def __init__(self, *args, **kwargs):
        self.fields = ('domain', 'feeding_points', 'discipline', 'description')
        super(FeedingFormSet, self).__init__(*args, **kwargs)
        self.queryset = Feeding.objects.filter(character=self.character, session=self.session)
        self.max_num = 1
        self.can_delete = True
        for form in self.forms:
            form.fields['discipline'].queryset = self.user.character.disciplines.all()
