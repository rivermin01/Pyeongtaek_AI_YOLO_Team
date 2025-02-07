import os
import shutil
import random

# 데이터셋 경로 설정
dataset_path = "C:/Users/Administrator/Desktop/data2/yolo11/coco8"  # 데이터셋 루트 폴더
image_path = os.path.join(dataset_path,"images")  # 이미지가 있는 폴더
label_path = os.path.join(dataset_path, "labels")  # 라벨이 있는 폴더

# Train 및 Val 폴더 생성
train_image_path = os.path.join(image_path, "train")
val_image_path = os.path.join(image_path, "val")
train_label_path = os.path.join(label_path, "train")
val_label_path = os.path.join(label_path, "val")

os.makedirs(train_image_path, exist_ok=True)
os.makedirs(val_image_path, exist_ok=True)
os.makedirs(train_label_path, exist_ok=True)
os.makedirs(val_label_path, exist_ok=True)

# 이미지 파일 리스트 가져오기
all_images = [f for f in os.listdir(image_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

# 데이터를 8:2로 랜덤하게 섞기
random.shuffle(all_images)
split_idx = int(len(all_images) * 0.9)  # 90%를 학습 데이터로 사용
train_images = all_images[:split_idx]
val_images = all_images[split_idx:]

# 이미지와 라벨 파일 이동 함수
def move_files(image_list, src_img_folder, src_lbl_folder, dest_img_folder, dest_lbl_folder):
    for img in image_list:
        img_name = os.path.splitext(img)[0]  # 확장자 제거한 파일명
        label_file = f"{img_name}.txt"

        # 이미지 이동
        shutil.move(os.path.join(src_img_folder, img), os.path.join(dest_img_folder, img))

        # 라벨 파일이 있으면 같이 이동
        if os.path.exists(os.path.join(src_lbl_folder, label_file)):
            shutil.move(os.path.join(src_lbl_folder, label_file), os.path.join(dest_lbl_folder, label_file))

# Train 데이터 이동
move_files(train_images, image_path, label_path, train_image_path, train_label_path)

# Val 데이터 이동
move_files(val_images, image_path, label_path, val_image_path, val_label_path)

print(f"✅ Train: {len(train_images)}개, Val: {len(val_images)}개 데이터 분리 완료!")
