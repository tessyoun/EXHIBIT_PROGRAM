from django.urls import path
from .views import *

app_name = 'ticket'

urlpatterns = [
    path('', ticket_list, name='ticket_list'),
    path('<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('purchase/', purchase_ticket, name='purchase_ticket'),
]