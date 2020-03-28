# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread(r"D:\testFiles\VR.jpg")
cv.imshow("img", img)
cv.waitKey(1000)
grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

'''ret,mask=cv.threshold(grayImg,127,255,cv.THRESH_BINARY_INV)
img1 = cv.bitwise_and(grayImg,grayImg,mask = mask)
#cv.imshow("img1",img1)
#cv.waitKey(1000)
#cv.imwrite(r"D:\testFiles\img1.jpg",img1)'''

rows,cols = grayImg.shape
roi = grayImg[0:700, 0:cols]
cv.imshow("ROI",roi)
cv.waitKey(2000)
cv.imwrite(r"D:\testFiles\ROI.jpg",roi)
ret,mask1=cv.threshold(roi,20,255,cv.THRESH_BINARY)
img2 = cv.bitwise_and(roi,roi,mask = mask1)
cv.imshow("img2",img2)
cv.waitKey(1000)
row,col = img2.shape
pixel_list = []
for i in range(row):
    for j in range(col):
        if img2[i,j] != 0:
            x =img2[i,j]
            pixel_list.append(x)
print(np.max(pixel_list))
print(np.mean(pixel_list))
print(np.median(pixel_list))

