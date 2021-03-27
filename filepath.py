
camera_Pic = "/home/pi/picam/pictures"
camera_Vid = "/home/pi/picam/videos"
camera_Log = "/home/pi/picam/logs"


def cameraPic(timeStamp):
    return camera_Pic + timeStamp + ".h264"


def cameraVid(timeStamp):
    return camera_Vid + timeStamp + ".h264"


def cameraLog(timeStamp):
    return camera_Log + timeStamp + ".h264"
