import os

camera_Pic = "/home/pi/picam/pictures/"
camera_Vid = "/home/pi/picam/videos/"
camera_Log = "/home/pi/picam/logs/"


def cameraPic(timeStamp):
    try:
        if os.makedirs(camera_Pic) == True:
            print("Path " + camera_Pic + " Already exist")


<< << << < HEAD
        else:
            os.makedirs(camera_Pic)
== == == =
            return camera_Pic + timeStamp + ".h264"
        else:
            os.makedirs(camera_Pic)
            return camera_Pic + timeStamp + ".h264"
>>>>>>> 4e905dfb2577020a77120b98d30efbbe0c8adda7
    except OSError as error:
        print("Directory '%s' can not be created")
    return camera_Pic + timeStamp + ".h264"


def cameraVid(timeStamp):
    try:
        if os.makedirs(camera_Vid) == True:
            print("Path " + camera_Vid + " Already exist")
        else:
            os.makedirs(camera_Vid)
            return camera_Vid + timeStamp + ".h264"
        else:
            os.makedirs(camera_Vid)
            return camera_Vid + timeStamp + ".h264"
    except OSError as error:
        print("Directory '%s' can not be created")
    return camera_Vid + timeStamp + ".h264"


def cameraLog(timeStamp):
    try:
        if os.makedirs(camera_Log) == True:
            print("Path " + camera_Log + " Already exist")
        else:
            os.makedirs(camera_Log)
            return camera_Log + timeStamp + ".h264"
        else:
            os.makedirs(camera_Log)
            return camera_Log + timeStamp + ".h264"
    except OSError as error:
        print("Directory '%s' can not be created")
    return camera_Log + timeStamp + ".h264"
