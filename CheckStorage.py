import subprocess
import shlex
import filepath


def checkSizeOfAllVidoes():
    totalSizeOfVid = subprocess.Popen(shlex.split('sudo du -sh videos/'))
    filepath.cameraLog(totalSizeOfVid)
    print(totalSizeOfVid)


def checkSizeOfAllPics():
    totalSizeOfPic = subprocess.Popen('sudo du -sh pictures/')
    filepath.cameraLog(totalSizeOfPic)
    print(totalSizeOfPic)
