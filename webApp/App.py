#-*-coding: utf-8 -*-
from flask import Flask, render_template,Response
from camera import Camera
from time import sleep
import os

#makeFlaskInstance
app=Flask(__name__, static_folder='./templates/images')

IMAGE_DIR="./templates/images"

def get_image(filename):
    with open(f"{IMAGE_DIR}/{filename}", "rb") as f:
        image = f.read()
    return image
    
    mtime = os.path.getmtime(f"{IMAGE_DIR}/{filename}")
    
    if mtime != last_mtime:
        last_mtime = mtime
        image = get_image(filename)
        
    return image
    

#showOnBrowser
@app.route('/')
def index():
    return render_template("test.html")

def gen(camera):
    while True:
        frame = camera.get_frame()

        if frame is not None:
            yield(b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
        else:
            print("frame is none")

@app.route("/video_feed")
def video_feed():
    return Response(gen(Camera()), mimetype="multipart/x-mixed-replace; boundary=frame")
    
@app.route("/image")
def image():
    while True:
        filename = "predict.jpeg"
        image = get_image(filename)
        return Response(image, mimetype="image/jpeg")
  
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
