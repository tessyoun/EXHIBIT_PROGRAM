from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.conf import settings
from django.core.serializers import serialize
from .models import Booth_Info
from .models import Exhibition_info, Exhibition
from .forms import ExhibitionForm
from .forms import BoothForm, ExhibForm

from mysite.models import ExhibitionInfo
from datetime import datetime

import json
import requests
import os
import base64
import cv2
import numpy as np
from mysite.settings import MEDIA_ROOT

PORT = 5000
AI_API_URL = 'https://8rgyr184rzf1v9-' + str(PORT) + '.proxy.runpod.net/generate'

# def getExhidb
booth_info = Booth_Info.objects.all()

# 이미지 경로 DB에 저장
@login_required
def save_layout(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        if 'data' in request.session:
            formdata = json.loads(request.session['data'])
            img_path = save_image_to_fileserver(image_data, formdata['exhibition_name'])
            if img_path:
                formdata['layout'] = img_path
                target = Exhibition.objects.get(exhibition_name=formdata['exhibition_name'])
                target.layout = img_path
                target.save()
                return JsonResponse({'img_path':img_path})
            else:
                return JsonResponse({'error': 'Failed to save image'}, status=500)
        else:
            return JsonResponse({'error': 'Failed to save image'}, status=500)

# 이미지 파일 저장 후 경로 반환
def save_image_to_fileserver(img_data, img_name):
    image = base64.b64decode(img_data)
    img_path = os.path.join(MEDIA_ROOT, img_name+'.png')

    with open(img_path, 'wb') as f:
        f.write(image)
    return img_path

# 전시회 객체 생성
@login_required
def create_exhibition(request):
    # 전시회 레이아웃 생성
    def render_image(session_data):
        response, images = get_image_from_server(session_data)
        if response.status_code == 200:
            return render(request, 'layout2.html', {'image_url': images})
        else:
            return JsonResponse({'error': 'Image rendering failed'}, status=response.status_code, safe=False)

    if request.method == 'POST':
        if request.user.is_staff:
            if 'data' in request.session and request.session['data']:
               return render_image(request.session['data'])
            else:
                form = ExhibitionForm(request.POST)
                if form.is_valid():
                    exhibition = form.save(commit=False)
                    exhibition.host_id = request.user.profile.name  # 로그인한 사용자의 아이디를 설정
                    exhibition.layout = '/'
                    exhibition.save()
                    request.session['data'] = create_json(form)
                    return render_image(request.session['data'])
                else:
                    print(form.errors) # 폼에러 확인
        else:
            return render(request, 'layout2.html', {'error':True})
    else:
        form = ExhibitionForm()
    return render(request, 'layout2.html', {'form': form, 'error':False})

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

@login_required
def update_exhibition(request):
    user_id = request.user.id
    # 현재 기업이 운영하는 전시회
    exhi = Exhibition_info.objects.filter(host_id=user_id).first()
    if request.method == 'POST':
        exhi_form = ExhibForm(request.POST, instance=exhi)
        if exhi_form.is_valid():
            exhi_form.save()
        return redirect('index')
    else:
        exhi_form = ExhibForm(instance=exhi)

    return render(request, 'exhibinfo.html', {'exhi_form':exhi_form})


# 배치도html 전처리, 생성
def process_image(request):     
    if 'data' not in request.session:
        print("Error: No session data found.")
        return None, []

    formdata = json.loads(request.session['data'])
    image_path = os.path.join(MEDIA_ROOT, formdata['exhibition_name'] +'.png')

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load the image file at {image_path}.")
        return None, []
    
    scale_percent = 100  # 이미지 크기 줄이기 가능 %
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 50, 100)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rectangles = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(image, [box], 0, (0, 255, 0), 2)
            rectangles.append((rect, box.tolist()))

    processed_image_path = os.path.join(settings.BASE_DIR, 'static/proceeded_images/test_image.png')
    cv2.imwrite(processed_image_path, resized_image)

    return 'proceeded_images/test_image.png', rectangles

def created_layout(request):
    image_path, rectangles = process_image(request)
    if image_path is None:
        return render(request, 'created_layout.html', {'error': 'Image processing failed.'})
    
    rectangles_with_dimensions = []
    for rect, box in rectangles:
        (center_x, center_y), (width, height), angle = rect
        if width < height:
            width, height = height, width
            angle += 90

        left = center_x - (width / 2)
        top = center_y - (height / 2)
        
        rectangles_with_dimensions.append({
            'left': left,
            'top': top,
            'width': width,
            'height': height,
            'rotate': angle,
            'center_x' : center_x,
            'center_y' : center_y,
        })

    booth = serialize('json', Booth_Info.objects.filter(exhibition_id=4))
    
    return render(request, 'created_layout.html', {'image_path': image_path, 
                                                    'rectangles': list(enumerate(rectangles_with_dimensions)),
                                                    'booths': booth,
                                                    })
