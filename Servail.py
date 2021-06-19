import recordVideo
import takePic
import filepath
from datetime import datetime
import time

now = datetime.now()
endDate = "06_23_2021_11:02:24"

stringNow = str(now)

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")





def rec(min, path):
    while stringNow != endDate:
        takePic.startPic()
        recordVideo.startRec(min, path)
        time.sleep(7200)
