import logging
import filepath
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")

logging.basicConfig(filename="/home/pi/picam/logs/" +
                    timeStamp, level=logging.INFO)


def writeToLog(logs):
    toWrite = open("/home/pi/picam/logs/" + timeStamp + ".log", "a")
    toWrite.write(logText(logs))
    toWrite.close()


def logText(logs):
    return str(logs)


# this gotta be fixed
# writeToLog(logging.info(timeStamp + "on"))
