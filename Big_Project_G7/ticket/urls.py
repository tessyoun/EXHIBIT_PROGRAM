from django.urls import path
from .views import *

app_name = 'tickets'

urlpatterns = [
    path('', reveal_QR, name='reveal_QR'),
]