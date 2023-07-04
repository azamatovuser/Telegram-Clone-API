from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import Account
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer, RoomWithMessagesSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404


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
        account_id = request.user.id
        room_id = request.data.get('room')
        message = request.data.get('message')
        if message and room_id and account_id:
            account = get_object_or_404(Account, id=account_id)
            room = get_object_or_404(Room, id=int(room_id))
            Message.objects.create(account=account, room=room, message=message)
            # channel_layer = get_channel_layer()
            # async_to_sync(channel_layer.group_send)(
            #     f'room_{room.id}',
            #     {
            #         'type': 'room_message',
            #         'message': message
            #     }
            # )
            return Response({"detail": "created"})
        return Response({"detail": "invalid data"})

        # Example of sending data
        # {
        #     "room": 1,
        #     "message": "message"
        # }