from django.urls import re_path
from chat import consumers

# that tells the client to listen to ws at consumers.py class
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]