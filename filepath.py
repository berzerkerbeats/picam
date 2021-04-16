import os
import logging
import toLogs

camera_Pic = "/home/pi/picam/pictures/"
camera_Vid = "/home/pi/picam/videos/"
camera_Log = "/home/pi/picam/logs/"


def cameraPic(timeStamp):

    print(str(os.path.isdir(camera_Pic)))
    cameraLog(logging.info(" Taking a picture "))

    if os.path.isdir(camera_Pic) == True:
        print()
        cameraLog(logging.info(
            " Path: " + camera_Pic + " Already exist"))
        return camera_Pic + timeStamp + ".jpg"

    else:
        os.makedirs(camera_Pic)
        return camera_Pic + timeStamp + ".jpg"

    cameraLog(logging.info(" Took a picture"))


def cameraVid(timeStamp):

    cameraLog(os.path.isdir(camera_Vid))
    cameraLog(logging.info(os.path.isdir(camera_Vid)))

    cameraLog(logging.info(os.path.isdir(camera_Vid)))

    cameraLog(logging.info(" Started Recording"))

    if os.path.isdir(camera_Vid) == True:
        cameraLog(logging.info(
            " Path: " + camera_Vid + " Already exist"))
        return camera_Vid + timeStamp + ".h264"

    else:
        os.makedirs(camera_Vid)
        return camera_Vid + timeStamp + ".h264"

    cameraLog(logging.info("Done Recording"))


def cameraLog(logs):
    try:
        if os.path.isdir(camera_Log) == False:
            cameraLog(logging.info(
                "Making Dir: " + camera_Log + " !"))
            os.makedirs(camera_Log)

        elif os.path.isdir(camera_Log) == True:
            toLogs.writeToLog(str(logs))
            return camera_Log + toLogs.timeStamp + ".log"

    except OSError:
        cameraLog(logging.critical("Could not make dir " +
                                   camera_Log + " check systems!!!"))

    try:
        print("Path: " + camera_Log + " Already exist")
        toLogs.writeToLog(str(logs))
        return camera_Log + toLogs.timeStamp + ".log"

    except OSError:
        pass
