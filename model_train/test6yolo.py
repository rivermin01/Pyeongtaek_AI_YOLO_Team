import os

train_dir = "C:/Users/Administrator/Desktop/test/datasets/coco8/images/train"
val_dir = "C:/Users/Administrator/Desktop/test/datasets/coco8/images/val"

print("Train 이미지 개수:", len(os.listdir(train_dir)))
print("Val 이미지 개수:", len(os.listdir(val_dir)))
