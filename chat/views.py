from rest_framework import generics
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer, RoomWithMessagesSerializer


class RoomListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/chat/rooms/
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomWithMessageAPIView(generics.RetrieveAPIView ):
    # http://127.0.0.1:8000/chat/rooms/room_id/
    queryset = Room.objects.all()
    serializer_class = RoomWithMessagesSerializer