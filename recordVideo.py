import picamera


def startRec():
    camera = picamera.PiCamera()
    camera.resolution = (1280, 720)
    camera.start_recording('test.h264')
    camera.wait_recording(10)
    camera.stop_recording()
