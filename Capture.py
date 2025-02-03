from ultralytics import solutions, YOLO
import cv2
from flask import Flask, Response

# YOLO 모델 로드
model = YOLO("yolo11n.pt")

status1 = 0
status2 = 0

# 비디오 스트리밍 함수 정의
def generate_frame():
    cap = cv2.VideoCapture(1)
    
    # 특정 좌표 설정
    region_points = {
        'region-01': [(10,100), (600,100), (100, 500)]
        # 'region-02': [(10,100), (600,100), (100, 500)]
    }

    # 구역 설정
    region = solutions.RegionCounter(
        show=True,
        region=region_points,
        model='yolo11n.pt'
    )
    
    
    while True:
        success, im0 = cap.read()
        if not success:
            print("프레임 확인")
            break
        
        region_results, counts = region.count(im0)
        print(f"count:{counts}")
        
        # 탐지된 객체의 수 추출
        global status1
        # global status2
        status1 = counts
        # status2 = region_results.count['region-02']
        
        # 프레임을 JPEG 형식으로 인코딩
        _, buffer = cv2.imencode('.jpg', region_results)
        # 인코딩된 이미지를 바이트 형태로 변환
        frame_bytes = buffer.tobytes()
        
        # 실시간으로 비디오 스트리밍 데이터 전송
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + 
               b'\r\n')
        
    cap.release()
    
def get_status1():
    return status1
def get_status2():
    return status2

