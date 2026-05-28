import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import Message

User=get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def get_user_info(self):
        return self.scope["user"].is_anonymous, self.scope["user"].id, self.scope["user"].username

    async def connect(self):
        print("🔥 CONNECT FUNCTION HIT")
        
        is_anonymous, user_id, username = await self.get_user_info()

        if is_anonymous:
            print("❌ Anonymous blocked")
            await self.close()
            return

        self.user_id = user_id
        self.username = username

        # Create a personal group for this user to receive messages from anyone
        self.user_group_name = f"user_{self.user_id}"
        print("JOINING GROUP:", self.user_group_name)

        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )

        await self.accept()
        print("✅ SOCKET CONNECTED")

    async def disconnect(self, close_code):
        print("❌ SOCKET DISCONNECTED")
        if hasattr(self, 'user_group_name'):
            await self.channel_layer.group_discard(
                self.user_group_name,
                self.channel_name
            )

    @database_sync_to_async
    def save_message(self, msg, receiver_id):
        receiver = User.objects.get(id=receiver_id)
        sender = User.objects.get(id=self.user_id)
        Message.objects.create(sender=sender, receiver=receiver, text=msg)
        return receiver.id

    async def receive(self, text_data):
        print("📩 RECEIVE CALLED")
        data = json.loads(text_data)
        
        msg = data.get("message")
        receiver_id = data.get("receiver_id")
        
        if not msg or not receiver_id:
            return

        print(f"MESSAGE: {msg} TO: {receiver_id}")

        # Push to receiver's websocket group
        receiver_group_name = f"user_{receiver_id}"
        await self.channel_layer.group_send(
            receiver_group_name,
            {
                "type": "chat_message",
                "message": msg,
                "sender_id": self.user_id,
                "sender_name": self.username
            }
        )
        print("📤 SENT TO RECEIVER GROUP (Real-time push)")

    async def chat_message(self, event):
        print("📨 PUSH TO BROWSER")
        await self.send(
            text_data=json.dumps({
                "message": event["message"],
                "sender_id": event["sender_id"],
                "sender_name": event["sender_name"]
            })
        )