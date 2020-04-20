import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Chat
from message.models import Message 
from message.serializers import MessageSerializer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
   
    def fetch_messages(self,data):
        
        messages = Message.objects.all().filter(chat__id=data['chat'])
        serializer = MessageSerializer(messages,many=True)
        content = {
            'command': 'messages',
            'messages' : serializer.data
        }
        self.send_message(content)
    

    def new_message(self,data):
        message = Message(
            content= str(data['message']['content'].replace("\n", " ")),
            contact_id= int(data['message']['contact']),
            chat_id=int(data['message']['chat'])
        )
        message.save()      
        serializer = MessageSerializer(message)
        content = {
            'command': 'new_message',
            'message': serializer.data
        }
        return self.send_chat_message(content)

    commands = {
        'fetch_messages' : fetch_messages,        
        'new_message' : new_message
    }


    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)        
        self.commands[data['command']](self,data)
    

    def send_chat_message(self,message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
