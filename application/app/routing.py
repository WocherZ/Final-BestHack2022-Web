from django.urls import path

from .consumers import *

ws_urlpatterns = [
    path('ws/news/', WSConsumerNews.as_asgi()),
    path('ws/rates/', WSConsumerRates.as_asgi()),
]
