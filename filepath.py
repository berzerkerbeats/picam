import os
import logging
import toLogs

camera_Pic = "/home/pi/picam/pictures/"
camera_Vid = "/home/pi/picam/videos/"
camera_Log = "/home/pi/picam/logs/"


def cameraPic(timeStamp):
    print(str(os.path.isdir(camera_Pic)))
    print("Gonna take a Pic")
    if os.path.isdir(camera_Pic) == True:
        print("Path: " + camera_Pic + " Already exist")
        return camera_Pic + timeStamp + ".jpg"
    else:
        os.makedirs(camera_Pic)
        return camera_Pic + timeStamp + ".jpg"
    print("Took a Pic")


def cameraVid(timeStamp):
    print(str(os.path.isdir(camera_Vid)))
    print(str(logging.info(os.path.isdir(camera_Vid))))
    cameraLog(logging.info(os.path.isdir(camera_Vid)))
    print("Started Recording")
    cameraLog(logging.info(" Started Recording"))
    logging.info("Started Recording")
    if os.path.isdir(camera_Vid) == True:
        print("Path: " + camera_Vid + " Already exist")
        return camera_Vid + timeStamp + ".h264"
    else:
        os.makedirs(camera_Vid)
        return camera_Vid + timeStamp + ".h264"
    print("Done Recording")
    cameraLog(logging.info("Done Recording"))

# have to create the logs dir mannually


def cameraLog(logs):

    if os.path.isdir(camera_Log):
        try:
            print("Path: " + camera_Log + " Already exist")
            #  camera_Log + timeStamp + ".log"
            return toLogs.writeToLog(logs)
        except OSError:
            pass
    else:
        os.makedirs(camera_Log)
        # camera_Log + timeStamp + ".log"
        return toLogs.writeToLog(logs)
