# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import os

def Ghost(inputImg):
    img = inputImg
    cv.imshow("img", img)
    cv.waitKey(100)
    grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,mask=cv.threshold(grayImg,150,255,cv.THRESH_BINARY_INV)
    img1 = cv.bitwise_and(grayImg,grayImg,mask = mask)
    cv.imshow("img1",img1)
    cv.waitKey(100)
    ret,mask1=cv.threshold(img1,50,255,cv.THRESH_BINARY)
    img2 = cv.bitwise_and(img1,img1,mask = mask1)
    cv.imshow("img2",img2)
    cv.waitKey(100)
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
    outPutData.write(str(np.max(pixel_list))+ "\n")
    outPutData.write(str(np.mean(pixel_list))+ "\n")
    outPutData.write(str(np.median(pixel_list))+ "\n")

path = "D:\\testFiles"
listDir = os.listdir(path)
print(listDir)

outPutData = open(path + "\\" + "Ghost_A.txt",'w')


for i in range(6):
    for dir in listDir:
        if dir == str(i+1) + "-a.jpg":
            print(path +"\\"+ dir)
            outPutData.write(path +"\\"+ dir + "\n")
            inputImg = cv.imread(path + "\\" + dir)
            Ghost(inputImg)




'''cv.imwrite(r"D:\testFiles\img1.jpg",img1)
rows,cols = img1.shape
roi = img1[0:700, 0:cols]
cv.imshow("ROI",roi)
cv.waitKey(3000)
cv.imwrite(r"D:\testFiles\ROI.jpg",roi)
ret,mask1=cv.threshold(roi,20,255,cv.THRESH_BINARY)
img2 = cv.bitwise_and(roi,roi,mask = mask1)
cv.imshow("img2",img2)
cv.waitKey(3000)
row,col = img2.shape
pixel_list = []
for i in range(row):
    for j in range(col):
        if img2[i,j] != 0:
            x =img2[i,j]
            pixel_list.append(x)
print(np.max(pixel_list))
print(np.mean(pixel_list))
print(np.median(pixel_list))'''
