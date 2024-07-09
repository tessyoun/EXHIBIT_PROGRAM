from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Program
from .forms import ProgramForm

@login_required
def program_open(request):
    if not request.user.profile.user_type == '기업회원' and not request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        form = ProgramForm(request.POST, user=request.user)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            company_name = request.user.profile.name
            selected_times = form.cleaned_data['selected_times']

            program = Program.objects.create(name=name, description=description, company_name=company_name, selected_times=selected_times)

            return redirect('index')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = ProgramForm(user=request.user)
    return render(request, 'program_open.html', {'form': form})
