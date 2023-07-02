from rest_framework import serializers, generics, permissions
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.pagination import PageNumberPagination


class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = PageNumberPagination
    page_size = 20
    permission_classes = [permissions.IsAuthenticated]


class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
