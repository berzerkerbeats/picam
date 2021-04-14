import recordVideo
import takePic
import time
import logging
import filepath


def main():
    recordVideo.startRec()
    filepath.cameraLog(str(logging.info(" Done Recording")))
    logging.info("Done Recording")
    time.sleep(5)
    takePic.startPic()
    filepath.cameraLog(str(logging.info(" Done with photo")))
    logging.info(" Done with photo")


if __name__ == '__main__':
    main()
