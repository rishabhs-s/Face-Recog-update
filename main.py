from flask import Flask, render_template, Response
from camera import VideoCamera


app = Flask(__name__)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/live')
def index():
    return render_template('index.html')



@app.route('/video_feed')

def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index1():
    return render_template("index1.html")

@app.route('/base')
def base():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)