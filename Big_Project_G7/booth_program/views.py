from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booth, Program, Reservation
from .forms import ProgramForm
from accounts.models import Profile  # Profile 모델을 임포트합니다.

@login_required
def program_open(request):
    if request.method == 'POST':
        # 수동으로 name과 description 필드를 추가하여 데이터를 설정합니다.
        data = request.POST.copy()
        data['name'] = data['booth_name']
        data['description'] = data['booth_description']

        # company_name을 수동으로 추가합니다.
        data['company_name'] = request.user.profile.name

        form = ProgramForm(data)
        if form.is_valid():
            booth_name = form.cleaned_data['booth_name']
            booth_description = form.cleaned_data['booth_description']
            company_name = request.user.profile.name  # 기업명을 현재 로그인된 사용자 이름으로 설정
            selected_times = data.get('selected_times').split(',')

            # 디버그 출력
            print(f"Booth Name: {booth_name}")
            print(f"Booth Description: {booth_description}")
            print(f"Company Name: {company_name}")
            print(f"Selected Times: {selected_times}")

            # Booth 인스턴스 생성 또는 가져오기
            booth, created = Booth.objects.get_or_create(name=booth_name, defaults={'description': booth_description, 'company_name': company_name})
            print(f"Booth Created: {created}, Booth ID: {booth.id}")

            # Program 인스턴스 생성
            program = Program.objects.create(booth=booth, name=booth_name, description=booth_description)
            print(f"Program ID: {program.id}")

            # Reservation 인스턴스 생성
            for time in selected_times:
                reservation = Reservation.objects.create(user=request.user, program=program, reserved_time=time)
                print(f"Reservation ID: {reservation.id}, Time: {time}")

            return redirect('index')
        else:
            # 폼 에러 메시지 출력
            print("Form is not valid")
            print(form.errors)
    else:
        form = ProgramForm()
    return render(request, 'program_open.html', {'form': form})

@login_required
def program_reservation(request):
    programs = Program.objects.all()
    if request.method == 'POST':
        program_id = request.POST.get('program_id')
        reserved_time = request.POST.get('reserved_time')
        program = Program.objects.get(id=program_id)
        Reservation.objects.create(user=request.user, program=program, reserved_time=reserved_time)
        retur
