from django.urls import path
from .views import *

app_name = 'ticket'

urlpatterns = [
    path('', ticket_list, name='ticket_list'),
    path('<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('purchase/', purchase_ticket, name='purchase_ticket'),
    path('cancel/<int:ticket_id>', cancel_ticket, name='cancel_ticket'),
    path('purchase/check_availableDate/<int:exhibition_id>', check_availableDate, name='check_availableDate')
]