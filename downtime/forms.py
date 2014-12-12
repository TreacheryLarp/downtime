from django.contrib.auth.forms import AuthenticationForm
from django import forms

from downtime.models import *

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super()
        if not user.character:
            raise forms.ValidationError(
                _('This user has no character.'),
                code='inactive',
            )

# Session submit forms
class SessionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Let us filter out disciplines that the character doesn't possess
        self.user = kwargs.pop('user')
        super(SessionForm, self).__init__(*args, **kwargs)

    def fill_save(self, session, character):
        o = self.save(commit=False)
        o.session = session
        o.character = character
        o.save()
        self.save_m2m()

class DisciplineActivationForm(SessionForm):
    class Meta:
        model = ActiveDisciplines
        fields = ['disciplines']

    def __init__(self, *args, **kwargs):
        super(DisciplineActivationForm, self).__init__(*args, **kwargs)
        self.fields['disciplines'].queryset = self.user.character.disciplines.all()

class ActionForm(SessionForm):
    class Meta:
        model = Action
        fields = ['action_type', 'description']

class FeedingForm(SessionForm):
    class Meta:
        model = Feeding
        fields = ['domain', 'feeding_points', 'discipline', 'description']

    def __init__(self, *args, **kwargs):
        # Let us filter out disciplines that the character doesn't possess
        super(FeedingForm, self).__init__(*args, **kwargs)
        self.fields['discipline'].queryset = self.user.character.disciplines.all()
