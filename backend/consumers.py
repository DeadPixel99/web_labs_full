import json
from pprint import pprint

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from backend.models import ConnectedUsers


class OnlineConsumer(WebsocketConsumer):

    def connect(self):
        ConnectedUsers.objects.create(sessionId=self.scope['cookies']['sessionid'])

    def disconnect(self, close_code):
        ConnectedUsers.objects.filter(sessionId=self.scope['cookies']['sessionid']).delete()


class TasksConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "finished_tasks"
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(text_data_json)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'task_message',
                'message': message
            }
        )

    def task_message(self, event):
        message = event['message']
        print(message)
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))