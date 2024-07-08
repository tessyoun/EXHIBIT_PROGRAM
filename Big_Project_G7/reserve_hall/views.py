from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm

def reserve_hall(request, hall_name):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reserve_hall:success')
        else:
            context = {
                'form': form,
                'hall_name': hall_name,
            }
            return render(request, 'reserve_hall.html', context)
    else:
        form = ReservationForm(initial={'hall_name': hall_name})
        context = {
            'form': form,
            'hall_name': hall_name,
        }
        return render(request, 'reserve_hall.html', context)

def success(request):
    return render(request, 'success.html')
