import qrcode
import base64

from io import BytesIO
from django.shortcuts import render

# QR코드 표 생성
def generate_QR(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    print('QR Generated!')
    return img

# 생성된 QR으로 표 예약 확인
def reveal_QR(request):
    dump_data = '에이블 1기 빅프로젝트 전시회_user_1명'
    qr = generate_QR(dump_data)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)
    img = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'tickets.html', {'image': img})