# -*- coding: utf-8 -*-

import cv2 as cv

image = cv.imread(r"D:\code\CV_Projects\MTF_1080.bmp")
output = "output"
cv.namedWindow(output, cv.WINDOW_NORMAL)
cv.resizeWindow(output, 1920, 1080)
cv.setWindowProperty(output, cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
cv.moveWindow(output,1920,0)
cv.imshow(output,image)
#cv.waitKey(0)


cap = cv.VideoCapture(0)
w = cap.get(3)          #获取长
h = cap.get(4)          #获取宽
print(w,h)
cap.set(3,1920)
cap.set(4,1080)

w = int(cap.get(3))
h = int(cap.get(4))
print(w,h)

center = (int(w/2),int(h/2))
print(center)

i = cap.get(15)         #获取曝光参数
i = -6                 #修改曝光参数
cap.set(15,i)           #设置曝光参数


while(cap.isOpened()):
    ret,frame = cap.read()
    output_frame = "output_frame"
    cv.namedWindow(output_frame, cv.WINDOW_NORMAL)
    cv.resizeWindow(output_frame, 1920, 1080)
    cv.setWindowProperty(output_frame, cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)


    cv.circle(frame,center,277,(0,0,255),thickness=3,lineType=8,shift=0)
    #cv.circle(frame, center, 554, (0, 0, 255), thickness=3, lineType=8, shift=0)
    #cv.circle(frame, center, 816, (0, 0, 255), thickness=3, lineType=8, shift=0)
    #cv.circle(frame, center, 1108, (0, 0, 255), thickness=3, lineType=8, shift=0)

    #中心十字线
    cv.line(frame,(int(w/2),0),(int(w/2),h),(0,0,255),thickness=2,lineType=8,shift=0)
    cv.line(frame,(0,int(h/2)),(w,int(h/2)),(0,0,255), thickness=2, lineType=8, shift=0)

    cv.putText(frame, "0", (960, 540), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 100, 0), 5)
    #cv.putText(frame, "10", (1237, 540), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 100, 0), 5)
    #cv.putText(frame, "20", (1514, 540), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 100, 0), 5)
    #cv.putText(frame, "30", (1791, 540), cv.FONT_HERSHEY_COMPLEX, 2.0, (0, 100, 0), 5)
    cv.putText(frame, "Exposure="+str(i), (300, 100), cv.FONT_HERSHEY_COMPLEX, 2.0, (100, 0, 0), 3)

    cv.imshow('output_frame',frame)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

cap.relese()
cv.destroyAllWindows()




