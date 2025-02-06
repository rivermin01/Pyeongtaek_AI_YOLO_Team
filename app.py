from flask import Flask, render_template, Response
from capture import generate_frame, get_status1, get_status2, get_status3

app = Flask(__name__)

# 실시간 화면 확인용
@app.route('/Video')
def video_feed():
    # 비디오 스트리밍 제공
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

'''
./templates/

blue.html:          파란 배경, 통행 가능
yellow.html:        노란 배경, 주의하며 통행 가능,                   1차 경고음(static/Ysound.mp3)
red.html:           빨간 배경, 통행 불가능,                        2차 경고음(static/Rsound.mp3)
---------------------------------------------------------------------------
yellow3.html(중앙용): 노란 배경, 2명, 1명으로 분할하여 통행,            안내 음성(static/y3.mp3)
yellow4.html(중앙용): 노란 배경, 2명, 2명으로 분할하여 통행,            안내 음성(static/y4.mp3)
red.html(중앙용):     빨간 배경, 2명씩 분할하여 통행, 남은 사람은 대기,    안내 음성(static/r5.mp3)
'''

# 1번 길 상황
@app.route('/road1')
def home1():
    while True:
        status = get_status1()          # 좌측 계단에 있는 사람의 수에 따라 각각 다른 HTML파일 불러오기
        if status <= 1:     # 1인 이하
            return render_template('blue.html')
        elif status == 2:   # 1인 이하
            return render_template('yellow.html')
        else:               # 3인 이상
            return render_template('red.html')

# 2번 길 상황
@app.route('/road2')
def home2():
    while True:
        status = get_status2()          # 우측 계단에 있는 사람의 수에 따라 각각 다른 HTML파일 불러오기
        if status <= 1:     # 1인 이하
            return render_template('blue.html')
        elif status == 2:   # 1인 이하
            return render_template('yellow.html')
        else:               # 3인 이상
            return render_template('red.html')
        
# 길 통제
@app.route('/road3')
def home3():
    while True:
        status = get_status3()          # 중앙 계단에 있는 사람의 수에 따라 각각 다른 HTML파일 불러오기
        if status <= 2:     # 2인 이하
            return render_template('blue.html')
        elif status == 3:   # 3인
            return render_template('yellow3.html')
        elif status == 4:   # 4인
            return render_template('yellow4.html')
        else:               # 5인 이상
            return render_template('red5.html')


# 애플리케이션 실행
if __name__ == "__main__":
    # Flask 서버를 실행
    app.run(host="0.0.0.0", port=5002, debug=True)
