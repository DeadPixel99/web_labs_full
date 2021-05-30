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