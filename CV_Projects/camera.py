# -*- coding: utf-8 -*-
import cv2 as cv

cap = cv.imread(r"C:\Users\李潇\Desktop\IMG_0011.bmp")
#cap = cv.VideoCapture(0,cv.CAP_DSHOW)
#cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('M', 'J', 'P', 'G'))
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

#cap.set(3,1920)
#cap.set(4,1080)

w = int(cap.get(3))
h = int(cap.get(4))
print(w,h)

center = (int(w/2),int(h/2))
print(center)

i = cap.get(15)         #获取曝光参数
i = -7                  #修改曝光参数
cap.set(15,i)           #设置曝光参数


while(cap.isOpened()):
    ret,frame = cap.read()

    cv.circle(frame,center,157,(0,0,255),thickness=3,lineType=8,shift=0)
    cv.circle(frame, center, 313, (0, 0, 255), thickness=3, lineType=8, shift=0)
    cv.circle(frame, center, 466, (0, 0, 255), thickness=1, lineType=8, shift=0)
    cv.circle(frame, center, 628, (0, 0, 255), thickness=1, lineType=8, shift=0)
    cv.circle(frame, center, 692, (0, 0, 255), thickness=1, lineType=8, shift=0)
    cv.circle(frame, center, 764, (0, 0, 255), thickness=1, lineType=8, shift=0)
    cv.circle(frame, center, 837, (0, 0, 255), thickness=1, lineType=8, shift=0)

    #中心十字线
    cv.line(frame,(int(w/2),0),(int(w/2),h),(0,0,255),thickness=2,lineType=8,shift=0)
    cv.line(frame,(0,int(h/2)),(w,int(h/2)),(0,0,255), thickness=2, lineType=8, shift=0)

    '''cv.putText(frame, "0", (960, 540), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 100, 0), 5)
    cv.putText(frame, "10", (1237, 540), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 100, 0), 5)
    cv.putText(frame, "20", (1514, 540), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 100, 0), 5)
    cv.putText(frame, "30", (1791, 540), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 100, 0), 5)'''
    cv.putText(frame, "Exposure="+str(i), (300, 100), cv.FONT_HERSHEY_COMPLEX, 2.0, (100, 0, 0), 3)
    cv.namedWindow("FullScreen", 0)
    cv.setWindowProperty("FullScreen", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow('FullScreen',frame)
    if cv.waitKey(1) & 0xff == ord('1'):
        break
    cv.imwrite("FOV_Test.jpg",frame)
cap.relese()
cv.destroyAllWindows()
