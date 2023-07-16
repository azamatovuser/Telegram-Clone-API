from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Room, Message
from account.serializers import MyProfileSerializer


class RoomSerializer(serializers.ModelSerializer):
    account = MyProfileSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ['id', 'account']

    def get_account(self, obj):
        account_ids = obj.members.all()
        account = get_user_model().objects.filter(id__in=account_ids)
        return account.values("id", "username")


class RoomMessageSerializer(serializers.ModelSerializer):
    account = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = "__all__"

    def get_account(self, obj):
        account_id = obj.account.id
        account = get_user_model().objects.get(id=account_id)
        return {"id": account.id, "username": account.username}


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'account', 'room', 'message']


class RoomWithMessagesSerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ['id', 'account', 'message']