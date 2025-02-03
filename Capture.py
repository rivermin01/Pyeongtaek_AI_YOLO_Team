from ultralytics import solutions, YOLO
import cv2
from flask import Flask, Response

# YOLO 모델 로드
model = YOLO("yolo11n.pt")

status = 0



# 비디오 스트리밍 함수 정의
def generate_frame():
    cap = cv2.VideoCapture(1)
    while True:
        success, frame = cap.read()
        if not success:
            print("프레임 확인")
            break
        
        # 객체 탐지
        results = model(frame)
        # 탐지 표시
        annotated_frame = results[0].plot()
        
        # 탐지된 객체의 수 추출
        detected_objects_count = len(results[0].boxes)  
        global status
        status = detected_objects_count  
        
        cv2.putText(annotated_frame, f'Status: {status}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # 프레임을 JPEG 형식으로 인코딩
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        # 인코딩된 이미지를 바이트 형태로 변환
        frame_bytes = buffer.tobytes()
        
        # 실시간으로 비디오 스트리밍 데이터 전송
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + 
               b'\r\n')
        
    
    
    
    cap.release()
    
def get_status():
    return status


