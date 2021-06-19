import picamera
import filepath


sec = 10



def startRec(sec, path):
    
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.start_recording(path)
        camera.wait_recording(sec)
        camera.stop_recording()
