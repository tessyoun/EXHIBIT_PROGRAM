from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

from accounts.models import Profile

from .models import Booth_Info
from .models import Exhibition_info
from .forms import ExhibitionForm
from .forms import BoothForm

import json
import requests

PORT = 5000
AI_API_URL = 'https://8rgyr184rzf1v9-' + str(PORT) + '.proxy.runpod.net/generate'

# def getExhidb
booth_info = Booth_Info.objects.all()

# 전시회 개최시 권한 바꿈(active>staff)
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
    # render generated image
    def render_image(session_data):
        response, images = get_image_from_server(session_data)
        if response.status_code == 200:
            return render(request, 'layout2.html', {'image_url': images})
        else:
            return response
        
    if request.method == 'POST':
        if request.session['data']:
           return render_image(request.session['data'])
        else:
            form = ExhibitionForm(request.POST)
            if form.is_valid():
                exhibition = form.save(commit=False)
                exhibition.host_id = request.user.profile.name  # 로그인한 사용자의 아이디를 설정
                exhibition.save()
                request.session['data'] = create_json(form)
                return render_image(request.session['data'])
            else:
                print(form.errors) # 폼에러 확인
    else:
        form = ExhibitionForm()
    return render(request, 'layout2.html', {'form': form})

# get generated Image from AI Server
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
            return JsonResponse({'Image generation failed from server'}, status=500), None
    
    except requests.exceptions.RequestException as E:
        return JsonResponse({'error': str(E)}, status=500), None

# create json file to generate booth layout
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

# 개최한 부스 리스트 가져오기
def booth_list(request):
    current_user_id = request.user.id # user_id
    exhibition_id = Exhibition_info.objects.filter(host_id=current_user_id).first()
    
    if exhibition_id:
        exhibition_id = exhibition_id.exhibition_id
        booths = Booth_Info.objects.filter(exhibition_id=exhibition_id).all()
    else:
        booths = []
    return render(request, 'booth_list.html', {'booths':booths})

# 부스 디테일
def detail(request, pk):
    booth = Booth_Info.objects.get(booth_id=pk)
    return render(request, 'detail.html', {'booths':booth})

# 부스 삭제
def delete(request, pk):
    booth = Booth_Info.objects.get(booth_id=pk)
    booth.delete()
    return redirect('booth_list.html')

# 부스 수정
def edit(request, pk):
    booth = Booth_Info.objects.get(booth_id=pk)
    return render(request, 'edit.html', {'booths':booth})

# 부스 업데이트
def update(request, pk):
    booth = Booth_Info.objects.get(booth_id=pk)
    booth.booth_name = request.POST.get('booth_name')
    booth.company_name = request.POST.get('company_name')
    booth.booth_category = request.POST.get('booth_category')
    booth.background = request.POST.get('background')
    booth.service = request.POST.get('service')
    booth.save()
    return redirect('detail', booth.pk)
    