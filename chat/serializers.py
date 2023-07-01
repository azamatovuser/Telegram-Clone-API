from rest_framework import serializers
from .models import Room, Message
from account.serializers import MyProfileSerializer


class RoomSerializer(serializers.ModelSerializer):
    account = MyProfileSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ['id', 'account']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'account', 'room', 'message']


class RoomWithMessagesSerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ['id', 'account', 'message']