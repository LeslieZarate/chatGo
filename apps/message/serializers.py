from rest_framework import serializers
from .models import Message
from contact.serializers import ContactUserSerializer

class MessageSerializer(serializers.ModelSerializer):
    contact  = ContactUserSerializer()
    class Meta:
        model = Message
        fields = '__all__'