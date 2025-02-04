import yaml

yaml_path = "C:/Users/Administrator/Desktop/test/coco8.yaml"

# YAML 파일 열기
with open(yaml_path, "r", encoding="utf-8") as f:
    data_config = yaml.safe_load(f)

# Train, Val 경로 출력
print("Train 데이터 경로:", data_config.get("train", "설정 없음"))
print("Validation 데이터 경로:", data_config.get("val", "설정 없음"))
