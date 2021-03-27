import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording('test.h264')
    camera.wait_recording(10)
    camera.stop_recording()
