from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer, RoomWithMessagesSerializer


class RoomListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/chat/rooms/
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     search = self.kwargs.get('search')
    #     if qs:
    #         qs = qs.filter(account__full_name__icontains=search)
    #     return qs


class RoomWithMessageAPIView(generics.RetrieveAPIView):
    # http://127.0.0.1:8000/chat/rooms/room_id/
    queryset = Room.objects.all()
    serializer_class = RoomWithMessagesSerializer


class MessageCreateAPIView(APIView):
    # http://127.0.0.1:8000/chat/rooms/message/create/
    def post(self, request):
        account = request.data.get('account')
        room = request.data.get('room')
        message = request.data.get('message')
        if message and room and account:
            Message.objects.create(account_id=account, room_id=room, message=message)
            return Response({"detail": "created"})
        return Response({"detail": "invalid data"})

    # Example of sending data
    # {
    #   "account":1,
    #   "room":5,
    #   "message":"test"
    # }