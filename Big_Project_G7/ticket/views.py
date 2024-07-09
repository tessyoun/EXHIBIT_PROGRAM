from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from exhibition.models import Exhibition_info
from .models import TicketBoughtInfo
from .functions import *
from .forms import *

import json

def get_ticket(userid) -> list:
    ticket_list = TicketBoughtInfo.objects.filter(user_id=userid)
    print(ticket_list)
    tickets = []
    for ticket in ticket_list:
        name = Exhibition_info.objects.get(exhibition_id=ticket.exhibitionid).exhibition_name
        key = ticket.ticketid
        tickets.append({'name':name, 'id':int(key)})
    return tickets

@login_required
def ticket_list(request):
    tickets = get_ticket(request.user.id)
    return render(request, 'check_ticket.html', {'ticket_list':tickets})

@login_required
def ticket_detail(request, ticket_id):
    if request.method == 'POST':
        img = generate_QR(json.dumps({'ticket_id':ticket_id}))
        return render(request, 'ticket_detail.html', {'image':img})
    else:
        return redirect('ticket:ticket_list')

@login_required
def purchase_ticket(request):
    if request.method == 'POST':
        form = TicketReservationForm(request.POST)
        if form.is_valid():
            userid = request.user.id
            reservation = form.save(commit=False)
            reservation.user_id = userid
            reservation.ticketid = int(''.join([str(userid),str(reservation.exhibitionid)]))
            reservation.save()

            return redirect('ticket:ticket_list')
    else:
        form = TicketReservationForm()

    return render(request, 'purchase_ticket.html', {'form': form})