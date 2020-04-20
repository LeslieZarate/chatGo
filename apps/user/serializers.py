from rest_framework import serializers
from contact.models import Contact
from .models import User


class UserSerializer(serializers.ModelSerializer):
    contact = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ['id','email','avatar','contact']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','avatar','username','first_name']