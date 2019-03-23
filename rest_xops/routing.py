# @Time    : 2019/3/13 10:56
# @Author  : xufqing
from websocket.jwt_auth import TokenAuthMiddleware
from channels.routing import URLRouter, ProtocolTypeRouter
from django.urls import path
#from websocket.consumers.deploy import DeployConsumer
from websocket.consumers.deploy_msg import DeployMsgConsumer

application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddleware(
        URLRouter([
            path(r"websocket/console", DeployMsgConsumer),
        ])
    )
})