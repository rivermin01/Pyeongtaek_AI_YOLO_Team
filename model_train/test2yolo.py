import cv2
import numpy as np
from ultralytics import YOLO

# YOLO 모델 로드 (사전 학습된 COCO 데이터셋 기반)
model = YOLO("yolo11n.pt")  # 또는 yolov8s.pt

# 비디오 파일 또는 웹캠 열기 (0: 웹캠, "video.mp4": 파일)
cap = cv2.VideoCapture("./test1.mp4")  # 비디오 파일
# cap = cv2.VideoCapture(0)  # 웹캠 사용 시

# 저장할 비디오 파일 설정
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # MP4 코덱
out = cv2.VideoWriter("output_video.mp4", fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# 비상구 위치 설정 (임의의 좌표)
exit_zone = [(100, 100), (500, 400)]  # (x1, y1), (x2, y2) 좌표
MAX_PEOPLE = 10  # 🚨 최대 허용 인원 (2명 이상이면 경고)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO 모델로 객체 감지
    results = model(frame)

    people_count = 0  # 감지된 사람 수

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # 바운딩 박스 좌표
            conf = box.conf[0]  # 신뢰도
            cls = int(box.cls[0])  # 클래스 ID

            # COCO 데이터셋 기준: 'person' 클래스 ID는 0
            if cls == 0 and conf > 0.5:
                # 비상구 영역 안에 있는 사람 감지
                if exit_zone[0][0] < x1 < exit_zone[1][0] and exit_zone[0][1] < y1 < exit_zone[1][1]:
                    people_count += 1
                    color = (0, 255, 0)  # 초록색 (정상)
                else:
                    color = (255, 0, 0)  # 파란색 (비상구 외부)

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)  # 사람 감지 박스 그리기

    # 비상구 영역 표시
    cv2.rectangle(frame, exit_zone[0], exit_zone[1], (0, 255, 255), 2)
    cv2.putText(frame, f"People in exit: {people_count}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # 🚨 2명 이상이면 경고 메시지 표시
    if people_count >= MAX_PEOPLE:
        cv2.putText(frame, "다른 계단을 이용하세요!", (100, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    # 결과 영상을 저장
    out.write(frame)

    # 영상 출력
    cv2.imshow("Exit Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()
