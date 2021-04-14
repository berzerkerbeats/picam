import logging
import filepath
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")

logging.basicConfig(format='%(levelname)s:%(message)s',  level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def writeToLog(logs):
    toWrite = open("/home/pi/picam/logs/" + timeStamp, "a")
    toWrite.write(logs)
    toWrite.close()


# this gotta be fixed
# writeToLog(logging.info(timeStamp + "on"))
