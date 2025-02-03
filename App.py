from ultralytics import YOLO
import cv2
from flask import Flask, Response

@app.route('/Video')
def video_feed():
    # 비디오 스트리밍 제공
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/road1')
def print():
    if status <= 2: 
        return "경로 사용 가능"
    else:
        return "경로 사용 불가능"
@app.route('/road2')
def print():
    if status <= 2: 
        return "경로 사용 가능"
    else:
        return "경로 사용 불가능"
