from rest_framework import serializers
from .models import Contact
from account.models import Account
from chat.models import Room, Message


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
