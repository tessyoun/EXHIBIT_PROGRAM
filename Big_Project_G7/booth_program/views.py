from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Program, BoothProgramReservation
from .forms import ProgramForm, ReservationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from exhibition.models import Booth_Info

# 홈 > 전시회 목록 > 전시회 > 부스 클릭 > 예약 클릭 시 생성된 부스 있는지 체크
def check_program(request, company_name):
    program_exists = Program.objects.filter(company_name=company_name).exists()
    if program_exists:
        booth = get_object_or_404(Booth_Info, company_name=company_name)
        return JsonResponse({'exists': True, 'booth_id': booth.booth_id})
    return JsonResponse({'exists': False})

# ----------------------------------------------------------------------------------------------------------------------------------
# (기업) 프로그램 생성
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

            print(f"Program created: {program}")

            return redirect('booth_program:program_choice')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ProgramForm()
    return render(request, 'program_open.html', {'form': form})

# (기업) 프로그램 > 프로그램 생성/관리
@login_required
def program_choice(request):
    return render(request, 'program_choice.html')

# (기업) 프로그램 > 예약 현황
@login_required
def reservation_status(request):
    user = request.user
    programs = Program.objects.filter(user=user)
    reservations = BoothProgramReservation.objects.filter(program__in=programs)
    sorted_reservations = sorted(reservations, key=lambda r: r.reservationtime_set.first().reserved_time)
    return render(request, 'reservation_status.html', {'reservations': sorted_reservations})

# (기업) 프로그램 > 프로그램 생성/관리 >  프로그램 관리
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
            return redirect('booth_program:program_manage')
    else:
        form = ProgramForm()

    return render(request, 'program_manage.html', {'form': form, 'programs': programs})

# (기업) 프로그램 > 프로그램 생성/관리 >  프로그램 관리 > 수정 및 삭제
@login_required
def program_edit(request, program_id):
    program = get_object_or_404(Program, id=program_id, user=request.user)
    time_slots = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    selected_times = program.selected_times.split(',') if program.selected_times else []

    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        print(form)
        print(form.is_valid(), form.has_changed())
        if form.is_valid():
            program = form.save(commit=False)
            new_selected_times = request.POST.get('selected_times', '')
            new_selected_times_list = sorted(list(set(new_selected_times.split(','))))
            print(new_selected_times_list)
            program.selected_times = ",".join(new_selected_times_list)
            program.save()
            return redirect('booth_program:program_manage')
        elif 'delete' in request.POST:
            program.delete()
            # return redirect('program_manage.html')
    else:
        form = ProgramForm(instance=program)
    
    return render(request, 'program_edit.html', {'form': form, 'time_slots': time_slots, 'selected_times': selected_times})

# ----------------------------------------------------------------------------------------------------------------------------------
# 부스에서 생성된 프로그램의 예약 가능한 시간 찾기
def get_availableTime(programID):
    timelist = Program.objects.get(id=programID).selected_times
    timetable = timelist.split(',')
    times = [(time, time) for time in timetable]
    return times

# (일반) 프로그램 예약
@login_required
def reserve_booth(request, booth_id):
    booth = get_object_or_404(Booth_Info, booth_id=booth_id)
    company_name = booth.company_name
    program_list = Program.objects.filter(company_name=company_name)

    if not program_list.exists():
        messages.error(request, '기업에서 프로그램을 생성하지 않았습니다.')
        return redirect('layout1')
    
    if request.method == 'POST':
        programID = request.POST.get('program_name')
        availableTime = get_availableTime(programID)
        form = ReservationForm(request.POST, programs=program_list, reservation_times=availableTime)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.user_name = request.user.username
            reservation.save()
            return redirect('booth_program:reservation_check')
        else:
            form = ReservationForm(programs = program_list)
    else:
        form = ReservationForm(programs = program_list)
    return render(request, 'reservation.html', {'form' : form, 'booth_id':booth_id})

# (일반) 프로그램 예약 시 기업이 오픈 한 시간만 리턴하는 API
def check_availableTime(request, program_id):
    if request.method == 'GET':
        try:
            program = Program.objects.get(id=program_id).selected_times
            timetable = program.split(',')
            times = [(time, time) for time in timetable]
            return JsonResponse({'times':times})

        except:
            return JsonResponse({'times': []})

# (일반) 마이페이지 > 내 예약 확인
@login_required
def reservation_check(request):
    user_name = request.user.username
    reservations = BoothProgramReservation.objects.filter(user_name=user_name).select_related('program')
    reserv_list = []
    for reservation in reservations:
        comp_name = reservation.program.company_name
        booth_name = Booth_Info.objects.get(company_name = comp_name).booth_name
        reserv_list.append({"com":comp_name, "boo":booth_name})
    content = zip(reservations, reserv_list)
    return render(request, 'reservation_check.html', {'reservations': content})

# (일반) 마이페이지 > 내 예약 확인 > 예약 삭제 API
@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(BoothProgramReservation, id=reservation_id, user_name=request.user.username)
    reservation.delete()
    return redirect('booth_program:reservation_check')

# (일반) 마이페이지 > 내 예약 확인 > 예약 수정 API
@login_required
@csrf_exempt
def edit_reservation(request, reservation_id):
    # reservation = get_object_or_404(BoothProgramReservation, id=reservation_id, user_name=request.user.username)
    # if request.method == 'POST':
    #     num_of_people = request.POST.get('num_of_people')
    #     reserved_time = request.POST.get('reserved_time')

    #     reservation.num_of_people = num_of_people
    #     reservation.reservationtime_set.update(reserved_time=reserved_time)
    #     reservation.save()

    #     return JsonResponse({'status': 'success'})
    # else:
    #     return JsonResponse({'status': 'fail', 'message': 'Invalid request method'})
    reservation = get_object_or_404(BoothProgramReservation, pk=reservation_id, user_name=request.user.username)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('booth_program:reservation_check')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'test.html', {'form': form})