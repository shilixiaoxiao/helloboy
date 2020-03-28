# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

#基础几何绘制
src=np.zeros([1080,1920,3],dtype=np.uint8) #创建窗口
cv.line(src,(10,10),(400,400),(255,0,0),1,cv.LINE_8,0) #线
cv.rectangle(src,(100,100),(400,400),(0,255,0),-1,cv.LINE_8,0) #正方形
cv.circle(src,(250,250),150,(0,0,255),4,cv.LINE_8,0) #圆
cv.ellipse(src,(250,250),(150,50),360,0,360,(255,234,0),3,cv.LINE_8,0) #椭圆
cv.putText(src,"Hello opencv",(50,50),cv.FONT_HERSHEY_PLAIN,1.2,(0,0,255),2,cv.LINE_8) #文字
#绘制多边形
points=[]
points.append((100,100))
points.append((150, 50))
points.append((200, 100))
points.append((200, 300))
points.append((100, 300))
index=0
for point in points:
    cv.line(src, point, points[(index+1)%5], (255, 0, 0), 3, cv.LINE_8, 0)
    index=index+1
cv.imshow("input",src)
cv.waitKey()
