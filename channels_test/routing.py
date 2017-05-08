# In routing.py
from channels.routing import route
from channels.routing import route
from .consumers import ws_message,ws_connect,ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message,path=r"^/$"),
    route("websocket.disconnect", ws_disconnect),
]