# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os

img = cv2.imread('D:\\testFiles\\1-b.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
orange_lower = np.array([100,43,46])
orange_upper = np.array([124,255,255]) #颜色色域
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #注意 一定要转换为hsv
mask = cv2.inRange(img_hsv,orange_lower,orange_upper) #mask 启动

#mask = cv2.erode(mask,None,iterations=2)
#mask = cv2.GaussianBlur(mask,(3,3),0)
#erode 和 GaussianBlur 是用来使得图片或视频更加模糊的 这样可以使得色彩突出更加明显，#色彩追踪也会更加精准

cv2.imshow('mask',mask)
cv2.waitKey(1000)
Ghost = cv2.bitwise_and(gray,gray,mask = mask)
ret,mask1=cv2.threshold(Ghost,10,255,cv2.THRESH_BINARY)
Ghost_B = cv2.bitwise_and(Ghost,Ghost,mask = mask1)
cv2.imshow("ghost",Ghost_B)
cv2.waitKey(1000)
row,col = Ghost_B.shape
pixel_list = []
for i in range(row):
    for j in range(col):
        if Ghost_B[i,j] != 0:
            x =Ghost_B[i,j]
            pixel_list.append(x)
print(np.max(pixel_list))
print(np.mean(pixel_list))
print(np.median(pixel_list))

'''img = cv2.imread("D:\\testFiles\\1-b.jpg",0)

#binaryImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binaryImg=cv2.threshold(img,40,255,cv2.THRESH_BINARY)
cv2.imshow("bIMG",binaryImg)
cv2.waitKey(3000)
#binaryImg = cv.Canny(gray,20,200)
#binary,contours,hierarchy = cv.findContours(gray,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

h = cv2.findContours(binaryImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


#提取轮廓
contours = h[0]
#打印返回值，这是一个元组
print(type(h))
#打印轮廓类型，这是个列表
print(type(h[1]))
#查看轮廓数量
print (len(contours))

#创建白色幕布
temp = np.ones(binaryImg.shape,np.uint8)*255
#画出轮廓：temp是白色幕布，contours是轮廓，-1表示全画，然后是颜色，厚度
cv2.drawContours(temp,contours,-1,(0,255,0),3)

cv2.imshow("contours",temp)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


