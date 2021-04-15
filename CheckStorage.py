import subprocess
import shlex
import filepath


def checkSizeOfAllVidoes():
    totalSizeOfVid = subprocess.Popen(shlex.split(
        ['home/pi/picam/videos/', '-cmd', "sudo du -sh"]))
    filepath.cameraLog(totalSizeOfVid)
    print(totalSizeOfVid)


def checkSizeOfAllPics():
    totalSizeOfPic = subprocess.Popen(["sudo du -sh home/pi/picam/pictures/"])
    filepath.cameraLog(totalSizeOfPic)
    print(totalSizeOfPic)
