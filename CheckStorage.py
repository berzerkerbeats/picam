import subprocess
import shlex
import filepath


def checkSizeOfAllVidoes():
    totalSizeOfVid = subprocess.Popen(shlex.split('sudo du -sh videos/'))
    filepath.cameraLog(str(totalSizeOfVid))
    print(totalSizeOfVid)


def checkSizeOfAllPics():
    totalSizeOfPic = subprocess.Popen(shlex.split('sudo du -sh pictures/'))
    filepath.cameraLog(str(totalSizeOfPic))
    print(totalSizeOfPic)


def checkSizeOfAllLogs():
    totalSizeOfPic = subprocess.Popen(shlex.split('sudo du -sh logs/'))
    filepath.cameraLog(str(totalSizeOfPic))
    print(totalSizeOfPic)
