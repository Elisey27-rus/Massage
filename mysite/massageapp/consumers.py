import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Логика для чтения писем и отправки прогресса
        for i in range(100):
            await self.send(text_data=json.dumps({'progress': i+1}))
