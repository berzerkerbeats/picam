import subprocess
from subprocess import check_output
import shlex
import filepath
import logging


def checkSizeOfAllVidoes():
    totalSizeOfVid = subprocess.Popen(shlex.split(
        'sudo du -sh videos/'), stdout=subprocess.PIPE, stderr=None, shell=True)
    stringOfTotalSizeOfVid = totalSizeOfVid.communicate()[0]
    # filepath.cameraLog(str(stringOfTotalSizeOfVid))
    print(totalSizeOfVid)
    print(logging.info(stringOfTotalSizeOfVid))


def checkSizeOfAllPics():
    totalSizeOfPic = subprocess.Popen(shlex.split(
        'sudo du -sh pictures/'), stdout=subprocess.PIPE, stderr=None, shell=True)
    stringOfTotalSizeOfPic = totalSizeOfPic.communicate()[0]
    # filepath.cameraLog(str(totalSizeOfPic))
    print(totalSizeOfPic)
    print(logging.info(stringOfTotalSizeOfPic))


def checkSizeOfAllLogs():
    totalSizeOfLogs = subprocess.Popen(shlex.split(
        'sudo du -sh logs/'), stdout=subprocess.PIPE, stderr=None, shell=True)
    stringOfTotalSizeOfLogs = totalSizeOfLogs.communicate()[0]
    # filepath.cameraLog(str(totalSizeOfLogs))
    print(totalSizeOfLogs)
    print(logging.info(stringOfTotalSizeOfLogs))
