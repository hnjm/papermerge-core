from django.urls import re_path

from .consumers import document as doc_consumer
from .consumers import nodes_move as nodes_move_consumer

websocket_urlpatterns = [
    re_path(
        r'ws/document/$',
        doc_consumer.DocumentConsumer.as_asgi()
    ),
    re_path(
        r'ws/nodes/move$',
        nodes_move_consumer.NodesMoveConsumer.as_asgi()
    ),
]