
from django.urls import path
from .views import LoginView ,UserView

app_name = 'user'
urlpatterns = [
    path('', LoginView.as_view(), name='login'), 
    path('users', UserView.as_view())
]