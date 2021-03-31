import logger as logging
import filepath
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")

logging.basicConfig(filename=filepath.camera_Log, filemode=str)
logging.info(timeStamp + "on")


def writeToLog(logs):
    toWrite = open(filepath.cameraLog(timeStamp), "a")
    toWrite.write(logText(logs))


def logText(logs):
    return str(logs)
