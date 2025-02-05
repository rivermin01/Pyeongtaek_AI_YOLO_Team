from flask import Flask, render_template, Response
from capture import generate_frame, get_status1, get_status2, get_status3

app = Flask(__name__)

# 실시간 화면 확인용
@app.route('/Video')
def video_feed():
    # 비디오 스트리밍 제공
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 1번 길 상황
@app.route('/road1')
def home1():
    while True:
        status = get_status1()
        if status <= 1:
            return render_template('blue.html')
        elif status == 2:
            return render_template('yellow.html')
        else:
            return render_template('red.html')

# 2번 길 상황
@app.route('/road2')
def home2():
    while True:
        status = get_status2()
        if status <= 1:
            return render_template('blue.html')
        elif status == 2:
            return render_template('yellow.html')
        else:
            return render_template('red.html')
        
# 길 통제
@app.route('/road3')
def home3():
    while True:
        status = get_status3()
        if status <= 2:
            return render_template('blue.html')
        elif status == 3:
            return render_template('yellow3.html')
        elif status == 4:
            return render_template('yellow4.html')
        else:
            return render_template('red5.html')


# 애플리케이션 실행
if __name__ == "__main__":
    # Flask 서버를 실행
    app.run(host="0.0.0.0", port=5002, debug=True)
