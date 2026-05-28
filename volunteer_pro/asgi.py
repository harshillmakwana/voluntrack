import os
from django.core.asgi import get_asgi_application

os.environ.setdefault(
"DJANGO_SETTINGS_MODULE",
"volunteer_pro.settings"
)

django_asgi_app=get_asgi_application()

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import app_modules.userapp.routing


application=ProtocolTypeRouter({

"http":django_asgi_app,

"websocket":
AuthMiddlewareStack(
URLRouter(
app_modules.userapp.routing.websocket_urlpatterns
)
),

})