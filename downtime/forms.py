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

class DisciplineActivationForm(forms.ModelForm):
    class Meta:
        model = ActiveDisciplines
        fields = ['disciplines']

    def __init__(self, *args, **kwargs):
        # Let us filter out disciplines that the character doesn't possess
        self.user = kwargs.pop('user')
        super(DisciplineActivationForm, self).__init__(*args, **kwargs)
        self.fields['disciplines'].queryset = self.user.character.disciplines.all()

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['action_type', 'description']

    def __init__(self, *args, **kwargs):
        # Let us filter out disciplines that the character doesn't possess
        self.user = kwargs.pop('user')
        super(ActionForm, self).__init__(*args, **kwargs)
