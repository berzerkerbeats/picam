import picamera
import filepath


def startRec():
    camera = picamera.PiCamera()
    camera.resolution = (1280, 720)
    camera.start_recording(filepath.cameraVid)
    camera.wait_recording(10)
    camera.stop_recording()
