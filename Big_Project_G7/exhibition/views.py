from django.shortcuts import render, redirect
from .models import exbooth_1st, exbooth_2nd, exbooth_3rd, exbooth_4th
from django.contrib.auth.decorators import login_required
from .models import Exhibition
from .forms import ExhibitionForm
from accounts.models import Profile


def getExhidb(exhi):
    exhibition = exhi.objects.all() # 1전시
    # exhi_2nd = exbooth_2nd.objects.all() # 2전시
    # exhi_3rd = exbooth_3rd.objects.all() # 3전시
    # exhi_4th = exbooth_4th.objects.all() # 4전시
    return exhibition

exhi_1st = getExhidb(exbooth_1st)
exhi_2st = getExhidb(exbooth_2nd)
exhi_3rd = getExhidb(exbooth_3rd)
exhi_4th = getExhidb(exbooth_4th)

@login_required
def create_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            exhibition = form.save(commit=False)
            exhibition.host_id = request.user.profile.name  # 로그인한 사용자의 아이디를 설정
            exhibition.save()
            return redirect('create_exhibition')
        else:
            print(form.errors) # 폼에러 확인
    else:
        form = ExhibitionForm()
    return render(request, 'layout2.html', {'form': form})

def change_perm(request):
    if request.method == 'POST':
        user = request.user
        user.is_staff = True
        user.save()
        return redirect('create_exhibition')

def create_layout():
    URL = 'https://8rgyr184rzf1v9-5000.proxy.runpod.net/generate'