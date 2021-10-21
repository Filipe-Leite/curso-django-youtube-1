from django                     import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obrigatório, digite um e-mail válido")

    class Meta:
        model   = User
        fields  = ("username", "email")