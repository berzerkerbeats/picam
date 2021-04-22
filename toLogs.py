import os
import logging
import filepath
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")

if os.path.isdir(filepath.camera_Log) == False:
    logging.info("Making Dir: " + filepath.camera_Log + " !")
    print("Making Dir: " + filepath.camera_Log + " !")
    logging.info("Made Dir !")
    print("Made Dir !")
    os.makedirs(filepath.camera_Log + timeStamp)

logging.basicConfig(filename="/home/pi/picam/logs/", format='%(asctime)s:%(message)s',  level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def writeToLog(logs):
    toWrite = open("/home/pi/picam/logs/" + timeStamp, "a")
    toWrite.write(logs)
    toWrite.close()
