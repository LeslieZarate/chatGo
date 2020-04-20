from django import forms
from django.contrib.auth.forms import AuthenticationForm

from user.models import User

class LoginForm(AuthenticationForm , forms.Form):
    birth_Date = forms.DateField(
        label = "Fecha de Nacimiento",
        widget=forms.TextInput(attrs={'size': '40'}),
    )
