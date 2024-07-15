from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse

from exhibition.models import Exhibition_info
from mysite.models import ExhibitionHall
from .models import TicketBoughtInfo
from .functions import *
from .forms import *

import json

# 로그인된 사용자의 티켓 조회
def get_ticket(userid) -> list:
    ticket_list = TicketBoughtInfo.objects.filter(user_id=userid)
    tickets = []
    for ticket in ticket_list:
        name = Exhibition_info.objects.get(exhibition_id=ticket.exhibitionid).exhibition_name
        key = ticket.ticketid
        tickets.append({'name':name, 'id':int(key)})
    tickets = sorted(tickets, key=lambda x: x['id'])
    return tickets

# 로그인된 사용자의 티켓 리스트
@login_required
def ticket_list(request):
    tickets = get_ticket(request.user.id)
    return render(request, 'check_ticket.html', {'ticket_list':tickets})

# 티켓 세부사항
@login_required
def ticket_detail(request, ticket_id):
    if request.method == 'POST':
        ticket = TicketBoughtInfo.objects.get(ticketid=ticket_id)
        exhibition = Exhibition_info.objects.get(exhibition_id=ticket.exhibitionid)
        exhibition_name = exhibition.exhibition_name
        hall = ExhibitionHall.objects.get(ExhibitionHallID=exhibition.hall_id).ExhibitionHallDescription
        adult = ticket.adult
        child = ticket.child
        username = request.user.username

        context = {'ticket_id':int(ticket_id), 'hall':hall, 'exhibition_name':exhibition_name,
                        'username':username, 'adult':adult, 'child':child}
        
        ticket_data = json.dumps(context, ensure_ascii=False)
        img = generate_QR(ticket_data)
        
        context['image'] = img
        print(context)
        return render(request, 'ticket_detail.html', context)
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
            ticketid = int(''.join([str(userid),str(reservation.exhibitionid)]))
            reservation.ticketid = ticketid

            if TicketBoughtInfo.objects.filter(ticketid=ticketid).exists():
                return ticket_detail(request, ticket_id=ticketid)
            else:
                reservation.save()
                return redirect('ticket:ticket_list')
                
    else:
        form = TicketReservationForm()

    return render(request, 'purchase_ticket.html', {'form': form})

@login_required
def cancel_ticket(request, ticket_id):
    if request.method == 'POST':
        TicketBoughtInfo.objects.get(ticketid=ticket_id).delete()
        return redirect('ticket:ticket_list')
    else:
        return redirect('ticket:ticket_list')
