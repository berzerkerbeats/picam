import recordVideo
import takePic
import time
import logging
import filepath
import CheckStorage


def main():
    recordVideo.startRec()
    logging.info(" Done Recording")
    time.sleep(5)
    takePic.startPic()
    logging.info(" Done with photo")
    CheckStorage.checkSizeOfAllVidoes()
    # CheckStorage.checkSizeOfAllPics()
    # CheckStorage.checkSizeOfAllLogs()


if __name__ == '__main__':
    main()
