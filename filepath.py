import os
import logging
import toLogs

camera_Pic = "/home/pi/picam/pictures/"
camera_Vid = "/home/pi/picam/videos/"
camera_Log = "/home/pi/picam/logs/"


def cameraPic(timeStamp):

    print(str(os.path.isdir(camera_Pic)))

    logging.info(" Taking a picture ")

    if os.path.isdir(camera_Pic) == True:
        logging.info(
            " Path: " + camera_Pic + " Already exist")
        return camera_Pic + timeStamp + ".jpg"

    else:
        os.makedirs(camera_Pic)
        return camera_Pic + timeStamp + ".jpg"

    logging.info(" Took a picture")


def cameraVid(timeStamp):

    logging.info(os.path.isdir(camera_Vid))

    logging.info(os.path.isdir(camera_Vid))

    logging.info(os.path.isdir(camera_Vid))

    logging.info(" Started Recording")

    print(" Started Recording")

    if os.path.isdir(camera_Vid) == True:
        logging.info(
            " Path: " + camera_Vid + " Already exist")
        return camera_Vid + timeStamp + ".h264"

    else:
        os.makedirs(camera_Vid)
        return camera_Vid + timeStamp + ".h264"

    logging.info("Done Recording")


def cameraLogMkdir():
    try:
        if os.path.isdir(camera_Log):
            logging.info("Making Dir: " + camera_Log + " !")
            print("Making Dir: " + camera_Log + " !")
            logging.info("Made Dir !")
            print("Made Dir !")
            os.makedirs(camera_Log + toLogs.timeStamp)

        elif os.path.isdir(camera_Log):
            logging.info("Path: " + camera_Log + " Already exist")

    except OSError:
        logging.critical("Could not make dir " +
                         camera_Log + " check systems!!!")
