from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer,ContactUserSerializer

class ContactView(generics.ListAPIView):
    serializer_class = ContactUserSerializer
    queryset = Contact.objects.all()

