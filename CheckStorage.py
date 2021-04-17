import subprocess
from subprocess import check_output
import shlex
import filepath


def checkSizeOfAllVidoes():
    totalSizeOfVid = subprocess.Popen(shlex.split('sudo du -sh videos/'))
    stringOfTotalSizeOfVid = totalSizeOfVid.communicate()[0]
    filepath.cameraLog(str(stringOfTotalSizeOfVid))
    print(totalSizeOfVid)


def checkSizeOfAllPics():
    totalSizeOfPic = subprocess.Popen(shlex.split('sudo du -sh pictures/'))
    stringOfTotalSizeOfPic = totalSizeOfPic.communicate()[0]
    filepath.cameraLog(str(totalSizeOfPic))
    print(totalSizeOfPic)


def checkSizeOfAllLogs():
    totalSizeOfLogs = subprocess.Popen(shlex.split('sudo du -sh logs/'))
    stringOfTotalSizeOfLogs = totalSizeOfLogs.communicate()[0]
    filepath.cameraLog(str(totalSizeOfLogs))
    print(totalSizeOfLogs)
