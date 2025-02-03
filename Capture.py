from ultralytics import solutions, YOLO
import cv2
from flask import Flask, Response

# Flask 애플리케이션 초기화
app = Flask(__name__)

# YOLO 모델 로드
model = YOLO("yolo11n.pt")


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
        status = detected_objects_count  
        
        if detected_objects_count<=1:
            status += " => 경로 사용 가능"
            color = (255, 0, 0) # 블루
        else:
            status += " => 경로 사용 불가능"
            color = (0, 0, 255) # 레드
        
        
        
        cv2.putText(annotated_frame, status, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        
        # 프레임을 JPEG 형식으로 인코딩
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        # 인코딩된 이미지를 바이트 형태로 변환
        frame_bytes = buffer.tobytes()
        
        # 실시간으로 비디오 스트리밍 데이터 전송
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + 
               b'\r\n')
        
    
    
    
    cap.release()
    
# Flask 라우트 정의
@app.route('/video')
def video_feed():
    # 비디오 스트리밍 제공
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 애플리케이션 실행
if __name__ == "__main__":
    # Flask 서버를 실행
    app.run(host="0.0.0.0", port=5001, debug=True)