# -*- coding: utf-8 -*-
import cv2 as cv


def video_demo():
    # 0是代表摄像头编号，只有一个的话默认为0
    cap = cv.VideoCapture(0)
    frame_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    frame_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    print(frame_height, frame_width)

    while (True):
        # 调用摄像机
        ref, frame = cap.read()
        frame = cv.resize(frame, (1920, 1080))
        # 输出图像,第一个为窗口名字
        cv.imshow('frame', frame)
        cv.line(frame, (0, 0), (260, 260), (255, 0, 0), 5)
        # 10s显示图像，若过程中按“Esc”退出,若按“s”保存照片并推出
        c = cv.waitKey(10) & 0xff
        if c == 27:
            # 简单暴力释放所有窗口
            cv.destroyAllWindows()
            break
        elif c == ord('s'):
            # 储存照片
            cv.imwrite('./images/pic.png', frame)
            break


if __name__ == '__main__':
    cv.waitKey()
    video_demo()

