from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import FormView,TemplateView
from rest_framework import viewsets

from contact.models import Contact
from .serializers import ChatSerializer
from .models import Chat
import json


class PageChatView(APIView):
    def get (self,request):
        user_contact =  Contact.objects.get(user=request.user.pk)        
        chat = Chat.objects.filter(participants__id=user_contact.id).order_by('-id')[:1]
        serializer = (ChatSerializer(chat,many=True).data[0])
          
        chat_obj = {
            "id": serializer['id']
        }
        if(serializer['type_chat'] == 2):
            chat_obj['name'] = serializer['name']
            chat_obj['avatar'] = serializer['avatar']
        else:
            for data in serializer['participants']:
                if data['id'] != user_contact.id: 
                    chat_obj['name'] = data['user']['username']
                    chat_obj['avatar'] = data['user']['avatar']

        return render(request, 'chat.html' , { 'user' : request.user , "user_contact" : user_contact , 'chat': chat_obj } )


class ChatView(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = ChatSerializer 
    queryset = Chat.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(participants__id=self.kwargs['pk_c']).order_by('-id')
        return queryset
      