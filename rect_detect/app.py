from flask import Flask, render_template, send_from_directory
import cv2
import numpy as np

app = Flask(__name__)

# Step 1: Load and process the image to detect rectangles
image_path = 'static/exhibition_layout11.png'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
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

# Save the processed image with rectangles for display
processed_image_path = 'static/processed_image.jpg'
cv2.imwrite(processed_image_path, image)

# Step 2: Set up the Flask server
@app.route('/')
def index():
    return render_template('index.html', image_path='processed_image.jpg', rectangles=rectangles, enumerate=enumerate)

@app.route('/image')
def get_image():
    return send_from_directory('static', 'processed_image.jpg')

if __name__ == '__main__':
    app.run(debug=True)
