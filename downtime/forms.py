from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super()
        if not user.character:
            raise forms.ValidationError(
                _("This user has no character."),
                code='inactive',
            )
