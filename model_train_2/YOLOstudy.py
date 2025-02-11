from ultralytics import YOLO

model = YOLO("yolo11n.pt")

#print(model.model) # yolo 11 모델 확인

model.train(data = "./COCO8.yaml", epochs = 50, batch =16, imgsz = 640, freeze = 22)