import picamera
import filepath
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")

sec = 10

path = filepath.cameraVid(timeStamp)

def startRec(self, sec, path):
    print(timeStamp)
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.start_recording(path)
        camera.wait_recording(sec)
        camera.stop_recording()
