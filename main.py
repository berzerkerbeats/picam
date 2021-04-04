import recordVideo
import takePic
import time


def main():
    recordVideo.startRec()
    time.sleep(5)
    takePic.startPic()


if __name__ == '__main__':
    main()
