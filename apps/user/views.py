from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView,TemplateView
from rest_framework import generics
from django.contrib.auth import authenticate,login

from .serializers import UserSerializer
from .models import User
from .forms import LoginForm
from django.http import HttpResponseRedirect

class LoginView(FormView):
    permission_class = ()
    form_class = LoginForm 
    template_name = "login.html" 
    success_url =  reverse_lazy('chat:page_chat') 

    def form_valid(self, form):
       email = form.cleaned_data['email']
       password = form.cleaned_data['password']
       user = authenticate(email=email, password=password)

       if user is not None and user.is_active:
           login(self.request, user)
           return HttpResponseRedirect(self.success_url)
       else:
           return self.form_invalid(form)




class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

