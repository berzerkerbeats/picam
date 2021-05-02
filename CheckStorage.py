import subprocess
from subprocess import check_output
import shlex
import filepath
import logging
import re


def checkSizeOfAllVidoes():
    totalSizeOfVid = subprocess.Popen(shlex.split(
        'sudo du -sh videos/'), stdout=subprocess.PIPE)
    stringOfTotalSizeOfVid = totalSizeOfVid.communicate()[0]
    print(stringOfTotalSizeOfVid)
    logging.info("The Current size is " + str(stringOfTotalSizeOfVid))
    video_string = re.match(r"\d", stringOfTotalSizeOfVid)
    print(video_string)


def checkSizeOfAllPics():
    totalSizeOfPic = subprocess.Popen(shlex.split(
        'sudo du -sh pictures/'), stdout=subprocess.PIPE)
    stringOfTotalSizeOfPic = totalSizeOfPic.communicate()[0]
    print(stringOfTotalSizeOfPic)
    logging.info("The Current size is " + str(stringOfTotalSizeOfPic))
    pic_string = re.match(r"\d", stringOfTotalSizeOfPic)
    print(pic_string)


def checkSizeOfAllLogs():
    totalSizeOfLogs = subprocess.Popen(shlex.split(
        'sudo du -sh logs/'), stdout=subprocess.PIPE)
    stringOfTotalSizeOfLogs = totalSizeOfLogs.communicate()[0]
    print(stringOfTotalSizeOfLogs)
    logging.info("The Current size is " + str(stringOfTotalSizeOfLogs))
    log_string = re.match(r"\d", stringOfTotalSizeOfLogs)
    print(log_string)
