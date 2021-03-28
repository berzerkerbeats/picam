import picamera
import filepath
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m/%d/%Y %H:%M:%S")

print(timeStamp)


def startRec():
    camera = picamera.PiCamera()
    camera.resolution = (1280, 720)
    camera.start_recording(filepath.cameraVid(timeStamp))
    camera.wait_recording(10)
    camera.stop_recording()
