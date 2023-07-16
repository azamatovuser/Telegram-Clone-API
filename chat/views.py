from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from account.models import Account
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer, RoomWithMessagesSerializer, RoomMessageSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticated


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None, **kwargs):
        chatroom = Room.objects.get(id=pk)
        serializer = RoomSerializer(chatroom)
        return Response(serializer.data)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = RoomMessageSerializer
    queryset = Message.objects.order_by("created_date")
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_id = self.request.query_params.get("room_id")
        if room_id is not None:
            return Message.objects.filter(room__id=room_id).order_by("created_date")
        else:
            return self.queryset


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

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class MessageCreateAPIView(APIView):
    # http://127.0.0.1:8000/chat/rooms/message/create/
    def post(self, request):
        account_id = request.user.id
        room_id = request.data.get('room')
        message = request.data.get('message')
        if message and room_id and account_id:
            account = get_object_or_404(Account, id=account_id)
            room = get_object_or_404(Room, id=int(room_id))
            Message.objects.create(account=account, room=room, message=message)
            return Response({"detail": "created"})
        return Response({"detail": "invalid data"})

        # Example of sending data
        # {
        #     "room": 1,
        #     "message": "message"
        # }


def lobby(request):
    return render(request, 'lobby.html')