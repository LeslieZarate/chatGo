from django.urls import path
from .views import * 

app_name = 'contact'
urlpatterns = [
    path('contacts', ContactView.as_view()), 
]