import recordVideo
import takePic
import time


def main():
    recordVideo.startRec()
    time.sleep(20)
    takePic.startPic()


if __name__ == '__main__':
    main()
