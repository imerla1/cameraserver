from flask import Flask, render_template, Response
from Camera import VideoCamera

app = Flask(__name__)

@app.route('/')  # TODO run in global
def index():
    return 'hello world'

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.50.100',port=50002, debug=True)