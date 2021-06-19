import recordVideo
import takePic
import filepath
from datetime import datetime

now = datetime.now()
endDate = "06_23_2021_11:02:24"

stringNow = str(now)

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")

min = 60

path = filepath.cameraVid(timeStamp)

def rec():
    while stringNow != endDate:
    takePic.startPic()
    recordVideo.startRec(min, path)
