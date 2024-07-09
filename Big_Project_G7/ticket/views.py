from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from exhibition.models import Exhibition_info
from .models import TicketBoughtInfo
from .functions import *

@login_required
def ticket_list(request):
    print(request.user)
    # if request.method == 'POST':
    if request.user:
        bought_list = TicketBoughtInfo.objects.get(request.user.id)
        print(bought_list)    
    return render(request, 'check_ticket.html', {'ticket_list':bought_list})

@login_required
def ticket_detail(request, key):
    if request.method == 'POST':
        img = generate_QR('test')
        return render(request, 'ticket_detail.html', {'image':img})
    return render(request, '')

@login_required
def buy_ticket(request):
    return render(request, 'test.html')