import subprocess
from subprocess import check_output
import shlex
import filepath
import logging


def checkSizeOfAllVidoes():
    totalSizeOfVid = subprocess.Popen(shlex.split(
        'sudo du -sh videos/'), stdout=subprocess.PIPE)
    stringOfTotalSizeOfVid = totalSizeOfVid.communicate()[0]
    # filepath.cameraLog(str(stringOfTotalSizeOfVid))
    print(stringOfTotalSizeOfVid)
    logging.info("The Current size is " + str(stringOfTotalSizeOfVid))


def checkSizeOfAllPics():
    totalSizeOfPic = subprocess.Popen(shlex.split(
        'sudo du -sh pictures/'), stdout=subprocess.PIPE)
    stringOfTotalSizeOfPic = totalSizeOfPic.communicate()[0]
    # filepath.cameraLog(str(totalSizeOfPic))
    print(stringOfTotalSizeOfPic)
    logging.info("The Current size is " + str(stringOfTotalSizeOfPic))


def checkSizeOfAllLogs():
    totalSizeOfLogs = subprocess.Popen(shlex.split(
        'sudo du -sh logs/'), stdout=subprocess.PIPE)
    stringOfTotalSizeOfLogs = totalSizeOfLogs.communicate()[0]
    # filepath.cameraLog(str(totalSizeOfLogs))
    print(stringOfTotalSizeOfLogs)
    logging.info("The Current size is " + str(stringOfTotalSizeOfLogs))
