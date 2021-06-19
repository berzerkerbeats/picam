import recordVideo
import takePic
import time
import logging
import filepath
import CheckStorage
import localh
import os
import Servail
from datetime import datetime

now = datetime.now()

timeStamp = now.strftime("%m_%d_%Y_%H:%M:%S")

now = datetime.now()
endDate = "06_23_2021_11:02:24"

stringNow = str(now)








    


path = filepath.cameraVid(timeStamp)

def main():
    
    filepath.cameraLogMkdir()
    time.sleep(0.5)
    recordVideo.startRec(5, path)
    logging.info(" Done Recording")
    print(" Done Recording")
    time.sleep(5)
    takePic.startPic()
    logging.info(" Done with photo")
    print(" Done with photo")
    CheckStorage.checkSizeOfAllVidoes()
    CheckStorage.checkSizeOfAllPics()
    CheckStorage.checkSizeOfAllLogs()
    print("found the storage size ")
    print("Starting....")
    while stringNow != endDate:
        takePic.startPic()
        recordVideo.startRec(min, path)
        time.sleep(3600)
    


if __name__ == '__main__':
    main()
