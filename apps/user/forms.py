from django import forms
from django.contrib.auth import authenticate

from user.models import User

class LoginForm(forms.ModelForm):
    class Meta:
       model = User
       fields = ['email','password']
       widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control' ,'placeholder': 'Email' , 'required':True}),
            'password': forms.PasswordInput(attrs={'class': 'form-control' ,'placeholder': 'Password' ,'required':True}),
        }
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not email and not password :
            raise forms.ValidationError('Completar los campos')
        else:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Ingrese correo electrónico y contraseña válida")
                
        return self.cleaned_data
