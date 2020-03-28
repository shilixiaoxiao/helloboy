# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

#基础几何绘制
src=np.zeros([1080,1920,3],dtype=np.uint8) #创建窗口
src.fill(255)
cv.rectangle(src,(0,0),(1920,54),(0,255,0),-1,cv.LINE_8,0)
cv.rectangle(src,(0,0),(96,1080),(0,255,0),-1,cv.LINE_8,0)
cv.rectangle(src,(0,1026),(1920,1080),(0,255,0),-1,cv.LINE_8,0)
cv.rectangle(src,(1824,0),(1920,1080),(0,255,0),-1,cv.LINE_8,0)
cv.rectangle(src,(960,0),(1056,540),(0,0,255),-1,cv.LINE_8,0)
cv.rectangle(src,(864,540),(960,1080),(255,0,0),-1,cv.LINE_8,0)

cv.imwrite(r"D:\distortion.bmp",src)
cv.namedWindow("src",cv.WINDOW_FULLSCREEN)
cv.imshow("src",src)
cv.waitKey(2000)