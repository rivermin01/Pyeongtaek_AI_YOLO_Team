from ultralytics import YOLO

# YOLO 모델 불러오기
model = YOLO("yolo11n.pt")

# 모델 구조 출력
print(model.model)