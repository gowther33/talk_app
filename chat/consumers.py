import json
from asgiref.sync import sync_to_async # for database
from channels.generic.websocket import AsyncWebsocketConsumer # for chat handling


class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scopre['url_route']['kwargs']['room_name'] # self.scope is request parameter in views
        self.room_group_name = f'chat_{self.room_name}'
        
        # Join Room
        await self.channel_layer.group_add(self.room_group_name, self.channel_layer)
        await self.accept()
    
    
    async def disconnect(self, code):
        # leave room
        await self.channel_layer.group_discard(self.room_group_name, self.channel_layer)
        