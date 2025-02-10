# 평택대학교 AI_YOLO팀 프로젝트
```
응급 상황 인파 밀집시 최적의 대피 경로
```
## 구성원
```
팀장 : 최강민
팀원 : 김병건, 이찬빈, 용석현, 신진수
```
## 설명
화재등 응급 대피 상황이 발생하였을 때, 원활한 대피를 위해 cctv를 통해 인파 밀집도를 분석한 후, 한 곳으로 몰리지 않도록 대피 경로를 조정해 준다.

### 실행 순서

![Image](https://github.com/user-attachments/assets/88080536-7386-47a0-a638-d182477d717f)

```
1. 코드를 실행하면 설정해둔 카메라를 통해 영상이 입력됩니다.
2. 미리 정해 둔 구역을 기준으로 각 구역에 사람의 수가 몇명인지를 계산을 하여 출력이 됩니다.
3. 출력된 프레임을 웹에서 보여주기 위해 JPEG로 인코딩을 실행합니다.
4. 인코딩 된 JPEG를 바이트 형태로 변환합니다.
5. 변환된 바이트를 플라스크에 실시간 비디오 스트리밍 데이터로 전송합니다.
6. 플라스크 앱을 실행시킵니다.
7. 플라스크 앱을 실행시키면 /Video에서 바이트로 스트리밍 받은 데이터를 비디오로 보여줍니다.
8. /road1, /road2, /road3에서 각 구역의 상황을 확인할 수 있습니다.
```

### 구조
```
127.0.0.1:5002/Video : 실시간 카메라 스트리밍
127.0.0.1:5002/road1 : 1번 길의 상황을 보여주는 화면 (좌측 계단)
127.0.0.1:5002/road2 : 2번 길의 상황을 보여주는 화면 (우측 계단)
127.0.0.1:5002/road3 : 3번 길의 상황을 보여주는 화면 (중앙 계단)
```

### 실시간 카메라 스트리밍 예시

### 각 구역의 상황 예시
<img width="811" alt="Image" src="https://github.com/user-attachments/assets/66badfd0-0c98-413f-986f-3cb23a21d740" />
```
```
<img width="811" alt="Image" src="https://github.com/user-attachments/assets/e79abec8-caed-43b1-a83f-27cd6ff30091" />
```
```
<img width="810" alt="Image" src="https://github.com/user-attachments/assets/eccd9cab-7399-41d7-944d-23b98fa0c2a4" />
```
```
<img width="812" alt="Image" src="https://github.com/user-attachments/assets/2e7d74db-b13d-4125-b58d-7881c984dd70" />
```
```
<img width="807" alt="Image" src="https://github.com/user-attachments/assets/930bc5b8-c351-48ab-ab64-ba03fb5dc07f" />
```
```
<img width="810" alt="Image" src="https://github.com/user-attachments/assets/6600b5f8-644f-49cf-af39-ed47b9a01dcf" />
```
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
