from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from exhibition.models import Exhibition_info
from .models import TicketBoughtInfo
from .functions import *
from .forms import *

import json

def get_ticket(ticket_list) -> list:
    tickets = []
    for ticket in ticket_list:
        name = Exhibition_info.objects.get(exhibition_id=ticket.exhibition_id).exhibition_name
        key = ticket.ticketid
        tickets.append({'name':name, 'id':int(key)})
    return tickets

@login_required
def ticket_list(request):
    bought_list = TicketBoughtInfo.objects.filter(user_id=request.user.id)
    tickets = get_ticket(bought_list)
    return render(request, 'check_ticket.html', {'ticket_list':tickets})

@login_required
def ticket_detail(request, ticket_id):
    if request.method == 'POST':
        img = generate_QR(json.dumps({'ticket_id':ticket_id}))
        return render(request, 'ticket_detail.html', {'image':img})
    return render(request, 'test.html')

@login_required
def purchase_ticket(request):
    if request.method == 'POST':
        form = TicketReservationForm(request.POST)
        print(1)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            print(2)
            return render(request, 'check_ticket.html')
    else:
        print(3)
        form = TicketReservationForm()
    print(4)
    return render(request, 'purchase_ticket.html', {'form': form})