import picamera
import filepath
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")


def startPic():
    print(timeStamp)
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(filepath.cameraPic(timeStamp))
