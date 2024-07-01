# mysite/views.py

import os
import cv2
import numpy as np
from django.shortcuts import render, redirect
from django.conf import settings
from accounts.forms import ProfileForm
from accounts.models import Profile

def process_image():
    image_path = os.path.join(settings.BASE_DIR, 'static/images/test1.png')
    
    if not os.path.exists(image_path):
        print(f"Error: The image file at {image_path} does not exist.")
        return None, []

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load the image file at {image_path}.")
        return None, []

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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

    processed_image_path = os.path.join(settings.BASE_DIR, 'static/proceeded_images/processed_image.jpg')
    cv2.imwrite(processed_image_path, image)

    return 'proceeded_images/processed_image.jpg', rectangles


def login_view(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def mypage(request):
    return render(request, 'mypage.html')

def layout1(request):
    image_path, rectangles = process_image()
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
        })

    return render(request, 'layout1.html', {'image_path': image_path, 'rectangles': list(enumerate(rectangles_with_dimensions))})

def layout2(request):
    return render(request, 'layout2.html')

def layout3(request):
    return render(request, 'layout3.html')

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

def reservation(request):
    return render(request, 'reservation.html')

def confirmation(request):
    user_type = request.user.profile.user_type  # 현재 로그인한 사용자의 user_type
    if user_type == '기업회원':
        return render(request, 'confirmation_busi.html')  # 기업회원일 경우 edit_booth.html 페이지 접속
    else:
        # 일반고객
        return render(request, 'confirmation.html')

@login_required
def memberinfo_view(request):
    user = request.user
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect('mypage')
    else:
        form = ProfileForm(instance=user.profile)

    return render(request, 'memberinfo.html', {'form': form})

# 배치도 생성하면 staff로 권한 바꿈
def change_permission(request):
    if request.method == 'POST':
        user = request.user
        user.is_staff = True
        user.save()
        return render(request, 'layout2.html')

# 추후에 기업 회원만 접근 가능하도록 수정 필요
def program_open(request):
    return render(request, 'program_open.html')