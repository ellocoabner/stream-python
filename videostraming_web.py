from flask import Flask
from flask import render_template
from flask import Response
import cv2

app = Flask(__name__)

cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml")

def generate():
    while True:
        ret,frame =cap.read()
        if ret: 
            gray= cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
            faces= face_detector.detecMultiScale(gray, 1.3, 5)
            for(x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y), (x+w. y+h)(0,255,0),2 )
                #comprime la imagen y la almacena en el bufer de memoria
            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            if not flag:
                continue
            yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' +
                  bytearray(encodedImage)+ b'\r\n')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(generate(),
                    mimetyoe="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    #seccion que activa el servidor de desarrollo
    app.run (debug=True)

cap.release()