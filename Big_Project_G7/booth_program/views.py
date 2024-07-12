from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Program
from .forms import ProgramForm

@login_required
def program_open(request):
    if not request.user.profile.user_type == '기업회원' and not request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            company_name = request.user.profile.name  # 작성자의 이름을 company_name에 저장
            selected_times = request.POST.getlist('selected_times')
            selected_times = sorted(set(selected_times))
            
            program = Program.objects.create(
                user=request.user,
                name=name,
                description=description,
                company_name=company_name,  # 작성자의 이름 저장
                selected_times=",".join(selected_times)
            )

            return redirect('program_manage')
        else:
            print("형식이 올바르지 않습니다")
            print(form.errors)
    else:
        form = ProgramForm()
    return render(request, 'program_open.html', {'form': form})

@login_required
def program_manage(request):
    programs = Program.objects.filter(user=request.user)  # 현재 사용자가 생성한 모든 프로그램 가져오기
    return render(request, 'program_manage.html', {'programs': programs})

@login_required
def program_edit(request, program_id):
    program = get_object_or_404(Program, id=program_id, user=request.user)
    time_slots = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    selected_times = program.selected_times.split(',') if program.selected_times else []

    if request.method == 'POST':
        if 'edit' in request.POST:
            form = ProgramForm(request.POST, instance=program)
            if form.is_valid():
                program = form.save(commit=False)

                new_selected_times = request.POST.getlist('selected_times')
                new_selected_times = sorted(list(set(new_selected_times)))

                program.selected_times = ",".join(new_selected_times)
                program.save()
                return redirect('program_manage')
        elif 'delete' in request.POST:
            program.delete()
            return redirect('program_manage')
    else:
        form = ProgramForm(instance=program)

    return render(request, 'program_edit.html', {'form': form, 'program': program, 'time_slots': time_slots, 'selected_times': selected_times})
