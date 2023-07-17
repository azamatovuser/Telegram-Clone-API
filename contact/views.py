from rest_framework import generics
from rest_framework.response import Response
from .models import Contact
from account.models import Account
from .serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework import status


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
