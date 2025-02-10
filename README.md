# Pyeongtaek_AI_YOLO_Team
Pyeongtaek_AI_YOLO_Team

## 평택대학교 AI_YOLO팀 프로젝트
```
응급 상황 인파 밀집시 최적의 대피 경로
```
## 구성원
```
팀장 : 최강민
팀원 : 김병건, 이찬빈, 용석현, 신진수
```
## 설명
### 요약
```
화재등 응급 대피 상황이 발생하였을 때, 원활한 대피를 위해 cctv를 통해 인파 밀집도를 분석한 후, 한 곳으로 몰리지 않도록 대피 경로를 조정해 준다.
```
### 구조
```
127.0.0.1:5002/Video : 실시간 카메라 스트리밍
127.0.0.1:5002/road1 : 1번 길의 상황을 보여주는 화면 (좌측 계단)
127.0.0.1:5002/road2 : 2번 길의 상황을 보여주는 화면 (우측 계단)
127.0.0.1:5002/road3 : 3번 길의 상황을 보여주는 화면 (중앙 계단)
```

## 환경 셋팅
The code requires python>=3.11.11 and we use Flask==3.1.0, ultralytics==8.3.66
```
Flask==3.1.0
numpy==2.2.2
opencv_python==4.11.0.86
Pillow==11.1.0
ultralytics==8.3.66

```
## 실행
```
1. zip 파일 다운
2. 압축 해제
3. 경로 설정(cd Pyeongtaek_AI_YOLO_Team)
4. 환경 셋팅
5. Pyeongtaek_AI_YOLO_Team/count.txt내용을 site-packages/ultralytics/solutions/region.counter.py로 옮기기
6. Pyeongtaek_AI_YOLO_Team/capture.py에서 Mac경로와 Window경로 확인하여 바꿔주기
6. python3 app.py
```
## 참고 자료 1
```
인파 밀집시 안내 문구를 알려주기 위해 Vrew 프로그램을 이용하여 AI로 보이스 생성
```
## 참고 자료 2
```
경고음을 로열티 프리에서 다운받아 사용
```
## 시연
```

```
