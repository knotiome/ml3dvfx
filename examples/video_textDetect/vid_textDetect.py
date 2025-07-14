import cv2
import easyocr

cap = cv2.VideoCapture('book.mp4')
reader = easyocr.Reader(['en'], gpu=True)

def detect_text(image):
    text_detections = reader.readtext(image)

    for t in enumerate(text_detections):
        print(t)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detect_text(gray)
    else:
        break

cap.release()