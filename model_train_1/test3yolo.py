import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont  # 한글 지원

# 🔹 한글 폰트 파일 경로 (Windows 기본 폰트 사용)
FONT_PATH = "C:/Windows/Fonts/malgun.ttf"  

# 🔹 YOLO 모델 로드 (사람만 감지할 것임)
model = YOLO("yolo11n.pt")  

# 🔹 비디오 파일 열기
cap = cv2.VideoCapture("./test1.mp4")  

# 🔹 결과 비디오 저장 설정
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  
out = cv2.VideoWriter("output_video.mp4", fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# 🔹 비상구 위치 설정
exit_zone = [(200, 200), (800, 700)]  
MAX_PEOPLE = 2  # 🚨 2명 이상이면 경고

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)  # YOLO 감지 실행
    people_count = 0  # 비상구 내 사람 수

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # 바운딩 박스 좌표
            conf = box.conf[0]  # 신뢰도
            cls = int(box.cls[0])  # 감지된 객체 클래스 ID

            # 🔹 '사람(person)' 클래스만 감지 (COCO dataset에서 ID 0번)
            if cls != 0:
                continue  # 사람이 아니면 무시

            # 🔹 비상구 영역 안에 있는 사람 수 계산
            if exit_zone[0][0] < x1 < exit_zone[1][0] and exit_zone[0][1] < y1 < exit_zone[1][1]:
                people_count += 1
                color = (0, 255, 0)  # 비상구 내 사람은 초록색 박스
            else:
                color = (255, 0, 0)  # 비상구 외부 사람은 빨간색 박스

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)  # 박스 그리기

    # 🔹 비상구 영역 시각화
    cv2.rectangle(frame, exit_zone[0], exit_zone[1], (0, 255, 255), 2)

    # 🔹 OpenCV → PIL 변환 (한글 폰트 지원)
    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(frame_pil)
    font = ImageFont.truetype(FONT_PATH, 40)  

    draw.text((50, 50), f"비상구 내 인원: {people_count}", font=font, fill=(255, 255, 255))

    # 🚨 2명 이상이면 경고 메시지 추가
    if people_count >= MAX_PEOPLE:
        draw.text((100, 100), "다른 비상구를 이용하세요!", font=font, fill=(255, 0, 0))

    # 🔹 PIL → OpenCV 변환 후 저장
    frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
    out.write(frame)
    cv2.imshow("Exit Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
