import cv2
import easyocr
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('book.mp4')
reader = easyocr.Reader(['en'], gpu=True)

w = int(cap.get(3))
h = int(cap.get(4))
out = cv2.VideoWriter('detections.mp4', cv2.VideoWriter_fourcc(*'mp4v'),30, (w,h), True)
threshold = 0.25

def detect_text(image):
    text_detections = reader.readtext(image)

    for i, t in enumerate(text_detections):
        print(t)
        bbox, text, score = t

        if score > threshold:
            start_point = tuple(map(int, bbox[0]))
            end_point = tuple(map(int, bbox[2]))
            cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
            cv2.putText(image, text, start_point, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        detect_text(frame)
        out.write(frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows