from django.shortcuts import render
from django.views.generic import FormView,TemplateView
from .forms import LoginForm
from rest_framework import generics

from .serializers import UserSerializer
from .models import User

class LoginView(FormView):
    form_class = LoginForm 
    template_name = "login.html"    

class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()