from ultralytics import YOLO

# 사전 학습된 YOLOv8 모델 불러오기 (YOLOv8n, YOLOv8s 등 선택 가능)
model = YOLO("yolo11n.pt")

# 모델 학습 수행
model.train(data="./coco8.yaml", epochs=50, batch=16, imgsz=640, freeze=22)
