from rest_framework import serializers
from .models import Contact
from user.serializers import UserDetailSerializer

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactUserSerializer(serializers.ModelSerializer):
    user  = UserDetailSerializer()
    class Meta:
        model = Contact
        exclude = ['friends']