import os

camera_Pic = "/home/pi/picam/pictures/"
camera_Vid = "/home/pi/picam/videos/"
camera_Log = "/home/pi/picam/logs/"


def cameraPic(timeStamp):
    try:
        if os.makedirs(camera_Pic) == True:
            print("Path " + camera_Pic + " Already exist")
        else:
            os.makedirs(camera_Pic)
    except OSError as error:
        print("Directory '%s' can not be created")
    return camera_Pic + timeStamp + ".h264"


def cameraVid(timeStamp):
    try:
        if os.makedirs(camera_Vid) == True:
            print("Path " + camera_Vid + " Already exist")
        else:
            os.makedirs(camera_Vid)
    except OSError as error:
        print("Directory '%s' can not be created")
    return camera_Vid + timeStamp + ".h264"


def cameraLog(timeStamp):
    try:
        if os.makedirs(camera_Log) == True:
            print("Path " + camera_Log + " Already exist")
        else:
            os.makedirs(camera_Log)
    except OSError as error:
        print("Directory '%s' can not be created")
    return camera_Log + timeStamp + ".h264"
