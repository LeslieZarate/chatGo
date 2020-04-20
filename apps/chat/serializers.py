from rest_framework import serializers
from chat.models import Chat
from contact.serializers import ContactUserSerializer

class ChatSerializer(serializers.ModelSerializer):
    participants = ContactUserSerializer(many=True)
    class Meta:
        model = Chat
        fields = '__all__'