from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Login ýa-da parol ýalňyş',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'id': 'username',
            'placeholder': 'Enter your username',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'id': 'password',
            'placeholder': 'Enter your password',
        })