# mysite/views.py

import os
import cv2
import numpy as np
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.serializers import serialize
from accounts.models import Profile
from .models import Booth_Info
from django.http import JsonResponse
import json


def max_pooling(image, pool_size):
    pooled_image = image[:image.shape[0] // pool_size * pool_size, :image.shape[1] // pool_size * pool_size]
    pooled_image = pooled_image.reshape(image.shape[0] // pool_size, pool_size, image.shape[1] // pool_size, pool_size)
    pooled_image = pooled_image.max(axis=(1, 3))
    return pooled_image

def process_image():
    image_path = os.path.join(settings.BASE_DIR, 'static/images/main.jpg')
    
    if not os.path.exists(image_path):
        print(f"Error: The image file at {image_path} does not exist.")
        return None, []

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

   # 지도 grid용 2d array// grayscale 이미지를 0(white) 1(black) 2d array로 변환
    _, bw_image = cv2.threshold(gray, 200, 1, cv2.THRESH_BINARY_INV)
    pool_size = 20
    pooled_image = max_pooling(bw_image, pool_size)
    
    bw_array = pooled_image.tolist()
    bw_array = [[1 - pixel for pixel in row] for row in bw_array]
    #

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

    processed_image_path = os.path.join(settings.BASE_DIR, 'static/proceeded_images/processed_image.jpg')
    cv2.imwrite(processed_image_path, resized_image)

    return 'proceeded_images/processed_image.jpg', rectangles, bw_array


def login_view(request):
    return render(request, 'login.html')

def index(request):
    booth = serialize('json', Booth_Info.objects.filter(exhibition_id=1))
    return render(request, 'index.html', {'booths': booth,})

def mypage(request):
    return render(request, 'mypage.html')

def reserve_exhib(request):
    return render(request, 'reserve_exhib.html')
    
def reveal_QR(request):
    return render(request, 'reveal_QR.html')

def layout1(request):
    image_path, rectangles, bw_array = process_image()
    if image_path is None:
        return render(request, 'layout1.html', {'error': 'Image processing failed.'})
    
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

    booth = serialize('json', Booth_Info.objects.filter(exhibition_id=1))
    
    return render(request, 'layout1.html', {'image_path': image_path, 
                                            'rectangles': list(enumerate(rectangles_with_dimensions)),
                                            'booths': booth,
                                            'bw_array': json.dumps(bw_array),  # Add this line
                                            })

def get_booth_info(request):
    booths = serialize('json', Booth_Info.objects.filter(exhibition_id=1))
    return JsonResponse(booths, safe=False)

def layout2(request):
    return render(request, 'layout2.html')

def about(request):
    items = [
        {'icon': 'images/Info_images/map_3753816.png',
         'alt': 'Icon 1',
         'title': '전시회 기획',
         'description': '전시회 개최 편의를 위해 부스 배치도 자동 생성 기능을 제공하고 있습니다.'},
        {'icon': 'images/Info_images/time-management_17048496.png',
         'alt': 'Icon 2',
         'title': '프로그램 관리 시스템',
         'description': '프로그램 예약관리를 통해 효율적인 부스 운영이 가능합니다.'},
        {'icon': 'images/Info_images/virtual-assistant_12692177.png',
         'alt': 'Icon 3',
         'title': '챗봇 서비스',
         'description': '전시회에 관한 질문에 신속하게 응답해드립니다.'},
        {'icon': 'images/Info_images/favourite_2374122.png',
         'alt': 'Icon 4',
         'title': '북마크 기능',
         'description': '관람 편의 향상을 위해 방문하고 싶은 부스를 북마크를 통해 한눈에 확인할 수 있습니다.'},
    ]
    return render(request, 'about.html', {'items': items})

def aivexhall(request):
    floors = [
        { 'floor_number': 'B1',
            'image': 'images/info_images/KTWest_리모델링설계안_희림건축 (3).jpg',
            'title': 'AIVEX MALL',
            'description': 'Aivex의 지하에 자리한 Aivex Mall, 현대적인 쇼핑과 편의시설이 만난 최고의 공간입니다. 다채로운 매장과 식사 옵션을 즐길 수 있는 중심지로, 편리하고 현대적인 쇼핑 경험을 제공합니다.'
        },
        {
            'floor_number': '1',
            'image': 'images/info_images/KTWest_리모델링설계안_희림건축 (7).jpg',
            'title': '만남의 광장',
            'description': 'Aivex의 만남의 광장, 다양한 사람들이 모여 소통하고 아이디어를 공유하는 혁신적인 공간입니다. 이곳은 문화적 다양성을 존중하며, 편안하고 개방적인 분위기에서 다양한 이벤트와 활동을 즐길 수 있는 장소입니다.'
        },
        {
            'floor_number': '2',
            'image': 'images/info_images/expo_hall_perchance_org_ai_generated (3).jpeg',
            'title': 'Hall A',
            'description': '2층에 위치한 A홀은 10,368㎡의 면적으로 최대 520개의 부스 설치가 가능하며 접근이 용이한 최적의 전시공간입니다. 친환경 전시시설을 자랑하는 AIVEX는 전시장조명을 LED로 교체하여 에너지 절감에 앞장서고 있으며, 콘크리트 바닥은 파이텍스 없이도 전시가 가능하게 하여 전시 폐기물을 최소화시키고 있습니다.'
        },
        {
            'floor_number': '2',
            'image': 'images/info_images/expo_hall_perchance_org_ai_generated (4).jpeg',
            'title': 'Hall B',
            'description': '2층에 위치한 B홀은 9,368㎡의 면적으로 최대 480개의 부스 설치가 가능하며 접근이 용이한 최적의 전시공간입니다. 친환경 전시시설을 자랑하는 AIVEX는 전시장조명을 LED로 교체하여 에너지 절감에 앞장서고 있으며, 콘크리트 바닥은 파이텍스 없이도 전시가 가능하게 하여 전시 폐기물을 최소화시키고 있습니다.'
        },
        {
            'floor_number': '3',
            'image': 'images/info_images/expo_hall_perchance_org_ai_generated (2).jpeg',
            'title': 'Hall C',
            'description': '3층에 위치한 C홀은 8,368㎡의 면적으로 최대 370개의 부스 설치가 가능하며 접근이 용이한 최적의 전시공간입니다. 친환경 전시시설을 자랑하는 AIVEX는 전시장조명을 LED로 교체하여 에너지 절감에 앞장서고 있으며, 콘크리트 바닥은 파이텍스 없이도 전시가 가능하게 하여 전시 폐기물을 최소화시키고 있습니다.'
        },
        {
            'floor_number': '3',
            'image': 'images/info_images/expo_hall_perchance_org_ai_generated (1).jpeg',
            'title': 'Hall D',
            'description': '3층에 위치한 D홀은 8,368㎡의 면적으로 최대 370개의 부스 설치가 가능하며 접근이 용이한 최적의 전시공간입니다. 친환경 전시시설을 자랑하는 AIVEX는 전시장조명을 LED로 교체하여 에너지 절감에 앞장서고 있으며, 콘크리트 바닥은 파이텍스 없이도 전시가 가능하게 하여 전시 폐기물을 최소화시키고 있습니다.'
        },
        {
            'floor_number': '4',
            'image': 'images/info_images/KTWest_리모델링설계안_희림건축 (2).jpg',
            'title': '회의실',
            'description': '4층은 총 12개의 중소형 회의실로 구성되어 있습니다. 전시장과 인접하여 위치하여 전시 부대 세미나, 기자회견, 소형 회의 등 다양한 용도로 활용할 수 있습니다. 일부 회의실에서는 외부 전경을 조망할 수 있는 특별한 장점도 있습니다.'
        },
        {
            'floor_number': '5',
            'image': 'images/info_images/KTWest_리모델링설계안_희림건축 (4).jpg',
            'title': '라운지',
            'description': '5층 라운지, 도시의 소외되지 않는 오아시스입니다. 현대적 디자인과 편안한 분위기 속에서 새로운 아이디어를 창출하고 사람들과의 연결을 즐길 수 있는 공간입니다.'
        }
    ]
    
    return render(request, 'aivexhall.html', {'floors': floors })

def layout4(request):
    return render(request, 'layout4.html')

def edit_profile_view(request):
    return render(request, 'edit_profile.html')

from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def edit_booth_view(request):
    user_type = request.user.profile.user_type  # 현재 로그인한 사용자의 user_type

    if user_type == '기업회원':
        return render(request, 'edit_booth.html')  # 기업회원일 경우 edit_booth.html 페이지 접속
    else:
        # 일반고객일 경우 페이지 접속 안됨
        messages.info(request, '접근 권한이 없습니다.') # 메세지 출력
        return render(request, 'mypage.html')  

def reservation(request, booth_id):
    booth = Booth_Info.objects.get(pk=booth_id)
    context = {
        'booth': booth
    }
    return render(request, 'reservation.html', context)

def confirmation(request):
    user_type = request.user.profile.user_type  # 현재 로그인한 사용자의 user_type
    if user_type == '기업회원':
        return render(request, 'confirmation_busi.html')  # 기업회원일 경우 edit_booth.html 페이지 접속
    else:
        # 일반고객
        return render(request, 'confirmation.html')

def program_open(request):
    return render(request, 'program_open.html')

def create_exhibition(request):
    return render(request, 'exhibition/templates/layout2.html')

# FAQ 검색 페이지
from chatgpt.models import faq_exhi
def FAQlist(request):
    faqs = faq_exhi.objects.all()  # Assuming FAQ is your model name

    for faq in faqs:
        if '?' in faq.qalist:
            faq.question, faq.answer = faq.qalist.split('?', 1)
        else:
            faq.question = faq.qalist
            faq.answer = ''

    context = {
        'faqs': faqs,
    }
    return render(request, 'FAQ.html', context)

def program_choice(request):
    return render(request, 'program_choice.html')

def program_manage(request):
    return render(request, 'program_manage.html')

