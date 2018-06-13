from django.contrib.auth import urls
from django.conf import settings

from . import views

app_name = "auth"
urlpatterns = [
   url(r'^login/$', views.user_login, name="user_login")
]

