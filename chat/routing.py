from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    #w+ means anything typed is accepted after chat/
    #/$ marks an end to the path beyond chat/room_name/
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]