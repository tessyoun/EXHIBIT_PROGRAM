# booth_program/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Program, BoothProgramReservation, ReservationTime
from .forms import ProgramForm, ReservationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from exhibition.models import Booth_Info

@login_required
def program_open(request):
    if not request.user.profile.user_type == '기업회원' and not request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            company_name = request.user.profile.name
            selected_times = form.cleaned_data['selected_times']

            print(f"Name: {name}, Description: {description}, Company: {company_name}, Selected Times: {selected_times}")

            selected_times_list = sorted(set(selected_times.split(',')))

            program = Program.objects.create(
                user=request.user,
                name=name,
                description=description,
                company_name=company_name,
                selected_times=",".join(selected_times_list)
            )

            return redirect('booth_program:program_choice')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ProgramForm()
    return render(request, 'program_open.html', {'form': form})


@login_required
def program_manage(request):
    programs = Program.objects.filter(user=request.user)
    
    if request.method == 'POST':
        if 'edit' in request.POST:
            program_id = request.POST.get('program_id')
            return redirect('booth_program:program_edit', program_id=program_id)
        elif 'delete' in request.POST:
            program_id = request.POST.get('program_id')
            program = get_object_or_404(Program, id=program_id, user=request.user)
            program.delete()
            return redirect('index')
    else:
        form = ProgramForm()

    return render(request, 'program_manage.html', {'form': form, 'programs': programs})

@login_required
def program_edit(request, program_id):
    program = get_object_or_404(Program, id=program_id, user=request.user)
    time_slots = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    selected_times = program.selected_times.split(',') if program.selected_times else []
    
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            program = form.save(commit=False)
            new_selected_times = request.POST.get('selected_times', '')
            new_selected_times_list = sorted(list(set(new_selected_times.split(','))))
            program.selected_times = ",".join(new_selected_times_list)
            program.save()
            return redirect('booth_program:program_manage')
        elif 'delete' in request.POST:
            program.delete()
            return redirect('booth_program:program_manage')
    else:
        form = ProgramForm(instance=program)
    
    return render(request, 'program_edit.html', {'form': form, 'time_slots': time_slots, 'selected_times': selected_times})

@login_required
def reserve_booth(request, booth_id):
    booth = get_object_or_404(Booth_Info, booth_id=booth_id)
    company_name = booth.company_name
    program_exists = Program.objects.filter(company_name=company_name).exists()

    if not program_exists:
        messages.error(request, '기업에서 프로그램을 생성하지 않았습니다.')
        return redirect('layout1')

    messages.success(request, '예약이 완료되었습니다.')
    return redirect('reservation', booth_id=booth_id)

def check_program(request, company_name):
    program_exists = Program.objects.filter(company_name=company_name).exists()
    if program_exists:
        booth = get_object_or_404(Booth_Info, company_name=company_name)
        return JsonResponse({'exists': True, 'booth_id': booth.booth_id})
    return JsonResponse({'exists': False})

@csrf_exempt
@login_required
def submit_reservation(request):
    if request.method == 'POST':
        user_name = request.user.username
        program_name = request.POST.get('program_name')
        num_of_people = int(request.POST.get('num_of_people'))
        reserved_time = request.POST.get('reserved_time')

        reservation = BoothProgramReservation.objects.create(
            user_name=user_name,
            program_name=program_name,
            num_of_people=num_of_people
        )

        ReservationTime.objects.create(
            reservation=reservation,
            reserved_time=reserved_time
        )

        return JsonResponse({'status': 'success', 'message': 'Reservation completed successfully'})

    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})

@login_required
def reservation_check(request):
    user_name = request.user.username
    reservations = BoothProgramReservation.objects.filter(user_name=user_name)
    return render(request, 'reservation_check.html', {'reservations': reservations})

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(BoothProgramReservation, id=reservation_id, user_name=request.user.username)
    reservation.delete()
    return redirect('booth_program:reservation_check')

@login_required
@csrf_exempt
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(BoothProgramReservation, id=reservation_id, user_name=request.user.username)
    if request.method == 'POST':
        num_of_people = request.POST.get('num_of_people')
        reserved_time = request.POST.get('reserved_time')

        reservation.num_of_people = num_of_people
        reservation.reservationtime_set.update(reserved_time=reserved_time)
        reservation.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})

@login_required
def program_choice(request):
    return render(request, 'program_choice.html')
