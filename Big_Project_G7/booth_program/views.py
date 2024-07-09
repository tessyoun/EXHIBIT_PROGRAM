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
            company_name = request.user.profile.name
            selected_times = form.cleaned_data['selected_times']

            program = Program.objects.create(
                user=request.user,
                name=name,
                description=description,
                company_name=company_name,
                selected_times=selected_times
            )

            return redirect('index')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ProgramForm()
    return render(request, 'program_open.html', {'form': form})


@login_required
def program_manage(request):
    program = get_object_or_404(Program, user=request.user)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = ProgramForm(request.POST, instance=program)
            if form.is_valid():
                form.save()
                return redirect('program_manage')
        elif 'delete' in request.POST:
            program.delete()
            return redirect('index')
    else:
        form = ProgramForm(instance=program)
    return render(request, 'program_manage.html', {'form': form, 'program': program})
