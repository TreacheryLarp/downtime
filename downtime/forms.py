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

    def fill_save(self):
        self.save_existing_objects(commit=True) # deletes objects
        instances = self.save(commit=False)
        for instance in instances:
            instance.session = self.session
            instance.character = self.character
            instance.save()
        self.save_m2m()


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
        super(ActionFormSet, self).__init__(*args, **kwargs)
        self.queryset = Action.objects.filter(character=self.character, session=self.session)
        extra_action_count = self.character.extra_action_count()
        self.extra = self.character.free_action_count() + extra_action_count
        self.max_num = self.extra
        # otherwise django might populate the forms with actions that
        # doest match their action_type queryset
        self.can_delete = False

        i = 0
        for extra_action in self.character.extra_actions():
            for j in range(extra_action.count):
                form = self.forms[i]
                form.fields['action_type'].queryset = extra_action.action_types.all()
                i = i + 1


class FeedingFormSet(SessionFormSet):

    def __init__(self, *args, **kwargs):
        super(FeedingFormSet, self).__init__(*args, **kwargs)
        self.queryset = Feeding.objects.filter(character=self.character, session=self.session)
        self.max_num = 1
        self.can_delete = True
        for form in self.forms:
            form.fields['discipline'].queryset = self.user.character.disciplines.all()
