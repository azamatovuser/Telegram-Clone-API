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


class ContactCreateGenericAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreateAPIView(APIView):
    def post(self, request):
        username = Account.objects.all()
        data = request.data
        print(3333333333, data)
        instance = Contact.objects.all()
        serializer = ContactSerializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
