from ultralytics import solutions, YOLO
import cv2
from flask import Flask, Response

# Flask 애플리케이션 초기화
app = Flask(__name__)

# YOLO 모델 로드
model = YOLO("yolo11n.pt")

status = 0

# 비디오 스트리밍 함수 정의
def generate_frame():
    cap = cv2.VideoCapture("rtsp://192.0.0.4:1935/")
    while True:
        success, frame = cap.read()
        if not success:
            print("프레임 확인")
            break
        
        # 객체 탐지
        results = model(frame)
        
        # 탐지된 객체의 수 추출
        detected_objects_count = len(results[0].boxes)  
        status = detected_objects_count  
        return status
    cap.release()
    
# Flask 라우트 정의
@app.route('/')
def print():
    if status <= 2: 
        return "경로 사용 가능"
    else:
        return "경로 사용 불가능"
    
# 애플리케이션 실행
if __name__ == "__main__":
    # Flask 서버를 실행
    app.run(host="0.0.0.0", port=5000, debug=True)