# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread(r"D:\testFiles\1-b.jpg")
grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.namedWindow('input_image',cv.WINDOW_NORMAL)
cv.imshow("input_image",grayImg)
cv.waitKey(500)
r = cv.selectROI("input_image", grayImg,showCrosshair= 0)
imCrop = grayImg[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv.imshow("imCrop",imCrop)
cv.waitKey(500)
ret,mask=cv.threshold(imCrop,20,255,cv.THRESH_BINARY)
img2 = cv.bitwise_and(imCrop,imCrop,mask = mask)
cv.imshow("img2",img2)
cv.waitKey(5000)
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
