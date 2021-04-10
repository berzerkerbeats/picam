import logging
import filepath
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def writeToLog(logs):
    toWrite = open("/home/pi/picam/logs/")
    toWrite.write(logs)
    toWrite.close()


def logText(logs):
    return str(logs)


# this gotta be fixed
# writeToLog(logging.info(timeStamp + "on"))
