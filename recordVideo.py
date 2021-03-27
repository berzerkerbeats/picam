import picamera
import filepath
import time

timeStamp = time.localtime()
print(timeStamp)


def startRec():
    camera = picamera.PiCamera()
    camera.resolution = (1280, 720)
    camera.start_recording(filepath.cameraVid(timeStamp))
    camera.wait_recording(10)
    camera.stop_recording()
