
from django.urls import path
from .views import LoginView ,UserView

app_name = 'user'
urlpatterns = [
    path('login', LoginView.as_view()), 
    path('users', UserView.as_view())
]