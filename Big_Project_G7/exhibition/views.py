from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse


from accounts.models import Profile

from .models import Booth_Info
from .models import Exhibition
from .forms import ExhibitionForm
from .forms import BoothForm

import json
import requests
import base64

PORT = 5000
# AI_API_URL = 'https://8rgyr184rzf1v9-' + str(PORT) + '.proxy.runpod.net/generate/once'
AI_API_URL = 'https://8rgyr184rzf1v9-' + str(PORT) + '.proxy.runpod.net/generate'

# def getExhidb
booth_info = Booth_Info.objects.all()

@login_required
def change_perm(request):
    if request.method == 'POST':
        user = request.user
        user.is_staff = True
        user.save()
        request.session['data'] = {}
        return redirect('create_exhibition')
    
# 전시회 객체 생성
@login_required
def create_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            exhibition = form.save(commit=False)
            exhibition.host_id = request.user.profile.name  # 로그인한 사용자의 아이디를 설정
            exhibition.save()
            request.session['data'] = create_json(form)
        elif not request.session['data']:
            print(form.errors) # 폼에러 확인

        response, images = get_image_from_server(request.session['data'])
        if response.status_code == 200:
            return render(request, 'layout2.html', {'image_url': images})
        else:
            return response
    else:
        form = ExhibitionForm()
    return render(request, 'layout2.html', {'form': form})

# 전시회 개최시 권한 바꿈(active>staff)
def get_image_from_server(data:json):
    try:
        response = requests.post(
            AI_API_URL,
            data = data,
            headers={'Content-type':'application/json'},
            timeout=200
        )

        if response.status_code == 200:
            images = response.json()
            return response, images
        else:
            return JsonResponse({'Image generation failed'}, status=500), None
    
    except requests.exceptions.RequestException as E:
        return JsonResponse({'error': str(E)}, status=500), None

def create_json(form):
    form_data = {
        'exhibition_name': form.cleaned_data['exhibition_name'] ,
        'hall': form.cleaned_data['hall'] ,
        'start_date':form.cleaned_data['start_date'] ,
        'end_date': form.cleaned_data['end_date'] ,
        'number_of_booths': form.cleaned_data['number_of_booths'] ,
    }
    json_data = json.dumps(form_data, cls=DjangoJSONEncoder, ensure_ascii = False)
    return json_data


@login_required
def update_booths(request):
    user_name = request.user.profile.name
    # 현재 기업이 운영하는 부스 정보
    
    booths_1st = Booth_Info.objects.filter(company_name=user_name, exhibition_id=1).first()
    booths_2nd = Booth_Info.objects.filter(company_name=user_name, exhibition_id=2).first()
    booths_3rd = Booth_Info.objects.filter(company_name=user_name, exhibition_id=3).first()
    booths_4th = Booth_Info.objects.filter(company_name=user_name, exhibition_id=4).first()

    if request.method == 'POST':
        form1 = BoothForm(request.POST, instance=booths_1st)
        form2 = BoothForm(request.POST, instance=booths_2nd)
        form3 = BoothForm(request.POST, instance=booths_3rd)
        form4 = BoothForm(request.POST, instance=booths_4th)

        if form1.is_valid() and booths_1st:
            form1.save()
        if form2.is_valid() and booths_2nd:
            form2.save()
        if form3.is_valid() and booths_3rd:
            form3.save()
        if form4.is_valid() and booths_4th:
            form4.save()

        messages.success(request, '부스 정보가 업데이트되었습니다.')
        return redirect('index')

    else:
        form1 = BoothForm(instance=booths_1st) if booths_1st else None
        form2 = BoothForm(instance=booths_2nd) if booths_2nd else None
        form3 = BoothForm(instance=booths_3rd) if booths_3rd else None
        form4 = BoothForm(instance=booths_4th) if booths_4th else None

    return render(request, 'boothinfo.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    })
