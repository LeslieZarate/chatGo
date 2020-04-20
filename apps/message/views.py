from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer


class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(chat__id=self.kwargs['pk_c']).order_by('-id')
        return queryset
      