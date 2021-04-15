import subprocess
import filepath


def checkSizeOfAllVidoes():
    totalSizeOfVid = subprocess.run("sudo du -sh home/pi/picam/videos/")
    filepath.cameraLog(totalSizeOfVid)
    print(totalSizeOfVid)


def checkSizeOfAllPics():
    totalSizeOfPic = subprocess.run("sudo du -sh home/pi/picam/pictures/")
    filepath.cameraLog(totalSizeOfPic)
    print(totalSizeOfPic)
