# mysite/views.py

import cv2
import os
from django.shortcuts import render
from django.conf import settings

def process_image():
    image_path = os.path.join(settings.BASE_DIR, 'static/images/test1.png')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 50, 100)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rectangles = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                rectangles.append((x, y, w, h))
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

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
    enumerated_rectangles = list(enumerate(rectangles))
    return render(request, 'layout1.html', {'image_path': image_path, 'rectangles': enumerated_rectangles})

def layout2(request):
    return render(request, 'layout2.html')

def layout3(request):
    return render(request, 'layout3.html')

def layout4(request):
    return render(request, 'layout4.html')

def edit_profile_view(request):
    return render(request, 'edit_profile.html')

def edit_booth_view(request):
    return render(request, 'edit_booth.html')

def reservation(request):
    return render(request, 'reservation.html')

def confirmation(request):
    return render(request, 'confirmation.html')
