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

from mysite.models import ExhibitionInfo
from datetime import datetime

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
        return redirect('exhibition:create_exhibition')
    
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
    booths = Booth_Info.objects.filter(company_name=user_name).first()

    if request.method == 'POST':
        form = BoothForm(request.POST, instance=booths)

        if form.is_valid() and booths:
            form.save()

        messages.success(request, '부스 정보가 업데이트되었습니다.')
        return redirect('index')

    else:
        form = BoothForm(instance=booths) if booths else None

    return render(request, 'boothinfo.html', {'form':form})

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
    return redirect('exhibition:detail', booth.pk)
    
    
# 전시회 목록 calendar 시작 페이지
def exhibition_list(request):
    exhibitions = ExhibitionInfo.objects.select_related('Hall_ID').values(
        'ExhibitionName', 'ExhibitionURL', 'Hall_ID__ExhibitionHallDescription',
        'ExhibitionRegistrationDate', 'ExhibitionClosedDate', 'ExhibitionImageURL'
    )
        
    exhibitions_list = list(exhibitions)
    for exhibition in exhibitions_list:
        exhibition['ExhibitionRegistrationDate'] = exhibition['ExhibitionRegistrationDate'].isoformat()
        exhibition['ExhibitionClosedDate'] = exhibition['ExhibitionClosedDate'].isoformat()
    
    exhibitions_json = json.dumps(exhibitions_list)
    
    return render(request, 'exhibition_list.html', {'exhibitions': exhibitions_json})

# # 전시회 목록 날짜별 불러오기
def exhibition_list_json(request, date=None):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    exhibitions = ExhibitionInfo.objects.filter(
        ExhibitionRegistrationDate__lte=date,
        ExhibitionClosedDate__gte=date
    ).select_related('Hall_ID').values(
        'ExhibitionName', 'ExhibitionURL', 'Hall_ID__ExhibitionHallDescription',
        'ExhibitionRegistrationDate', 'ExhibitionClosedDate', 'ExhibitionImageURL'
    )
    
    exhibitions_list = list(exhibitions)
    for exhibition in exhibitions_list:
        exhibition['ExhibitionRegistrationDate'] = exhibition['ExhibitionRegistrationDate'].isoformat()
        exhibition['ExhibitionClosedDate'] = exhibition['ExhibitionClosedDate'].isoformat()
    
    return JsonResponse(json.dumps(exhibitions_list), safe=False)