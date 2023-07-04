from channels.generic.websocket import AsyncWebsocketConsumer
import json


class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = f'room_{self.scope["url_route"]["kwargs"]["room_id"]}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'room_message',
                'message': message
            }
        )

    async def room_message(self, event):
        # Receive message from room group
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
