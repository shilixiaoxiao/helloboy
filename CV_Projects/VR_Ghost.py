# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

Img = cv.imread(r"D:\VR.jpg")
ImgGray = cv.cvtColor(Img, cv.COLOR_BGR2GRAY)
ret,thresh1=cv.threshold(Img,127,255,cv.THRESH_BINARY)
kernel = cv.getStructuringElement(cv.MORPH_RECT,(3, 3))
dilated = cv.dilate(thresh1,kernel)
#cv.namedWindow('dilated',cv.WINDOW_NORMAL)
#cv.imshow("thresh1",thresh1)
#cv.imshow("dilated",thresh1)
#cv.waitKey(3000)

bitwiseNot = cv.bitwise_not(dilated)
#cv.imshow("bitwiseNot",bitwiseNot)
#cv.waitKey(1000)
bitwiseAnd = cv.bitwise_and(Img,bitwiseNot)
#cv.imshow("bitwiseAnd",bitwiseAnd)
#cv.waitKey(3000)
ret,thresh2=cv.threshold(bitwiseAnd,40,255,cv.THRESH_BINARY)
cv.namedWindow('thresh2',cv.WINDOW_NORMAL)
cv.imshow("thresh2",thresh2)
cv.waitKey(30000)
