
from django.urls import path
from .views import LoginView ,UserView ,LogoutView

app_name = 'user'
urlpatterns = [
    path('', LoginView.as_view(), name='login'), 
    path('logout', LogoutView.as_view(), name='logout'), 
    path('users', UserView.as_view())
]