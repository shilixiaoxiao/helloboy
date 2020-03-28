# -*- coding: utf-8 -*-
import cv2 as cv
import time

#cap = cv.VideoCapture(0,cv.CAP_DSHOW)
cap = cv.VideoCapture(0)
#cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('M', 'J', 'P', 'G'))
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
#cap.set(3,1920)
#cap.set(4,1080)
w = int(cap.get(3))
h = int(cap.get(4))
#print(w,h)
center = (int(w/2),int(h/2))
print(center)

i = cap.get(15)         #获取曝光参数
i = -7                  #修改曝光参数
cap.set(15,i)           #设置曝光参数

while(cap.isOpened()):
    ret,frame = cap.read()

    cv.circle(frame, center, 161, (0, 0, 255), thickness=3, lineType=8, shift=0)
    cv.circle(frame, center, 322, (0, 0, 255), thickness=3, lineType=8, shift=0)
    cv.circle(frame, center, 481, (0, 0, 255), thickness=2, lineType=8, shift=0)
    cv.circle(frame, center, 646, (0, 0, 255), thickness=2, lineType=8, shift=0)
    cv.circle(frame, center, 712, (0, 0, 255), thickness=2, lineType=8, shift=0)
    cv.circle(frame, center, 785, (0, 0, 255), thickness=2, lineType=8, shift=0)
    cv.circle(frame, center, 858, (0, 0, 255), thickness=2, lineType=8, shift=0)

    # 中心十字线
    cv.line(frame, (int(w / 2), 0), (int(w / 2), h), (0, 0, 255), thickness=2, lineType=8, shift=0)
    cv.line(frame, (0, int(h / 2)), (w, int(h / 2)), (0, 0, 255), thickness=2, lineType=8, shift=0)

    cv.putText(frame, "0", (930, 520), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 100, 0), 3)
    cv.putText(frame, "20", (769, 520), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 100, 0), 3)
    cv.putText(frame, "40", (608, 520), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 100, 0), 3)
    cv.putText(frame, "60", (449, 520), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 100, 0), 3)
    cv.putText(frame, "80", (284, 520), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 100, 0), 3)
    cv.putText(frame, "90", (218, 520), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 100, 0), 3)
    cv.putText(frame, "100", (145, 520), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 100, 0), 3)
    cv.putText(frame, "110", (72, 520), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 100, 0), 3)

    cv.putText(frame, "Exposure=" + str(i), (300, 100), cv.FONT_HERSHEY_COMPLEX, 2.0, (200, 0, 0), 3)
    cv.namedWindow("FullScreen", 0)
    cv.setWindowProperty("FullScreen", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow('FullScreen', frame)
    if cv.waitKey(1) & 0xff == ord('1'):
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(nowTime)

        cv.imwrite("VR_FOV_" + str(nowTime) + ".bmp", frame)
        break
cap.relese()
cv.destroyAllWindows()
