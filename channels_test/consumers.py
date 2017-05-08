from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

def ws_message_old(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    message.reply_channel.send({
        "text": message.content['text'],
    })

# Connected to websocket.receive
def ws_message(message):
    print 'in message'
    Group("ntly-map").send({
        #"text": "[user] %s" % message.content['text'],
        "text": message.content['text'],
    })

# Connected to websocket.connect
def ws_connect(message):
    print 'in connect'
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    # Add them to the chat group
    Group("ntly-map").add(message.reply_channel)

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("ntly-map").discard(message.reply_channel)