import qrcode
import base64

from io import BytesIO

# QR코드 생성
def generate_QR(data):
    buffer = BytesIO()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    tmp = qr.make_image(fill_color="black", back_color="white")
    tmp.save(buffer, format='PNG')
    buffer.seek(0)
    img = base64.b64encode(buffer.getvalue()).decode()
    return img
