# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt

#for dir_src in listDir:

img = cv.imread("D:\\testFiles\\Phone_B.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 挖去中心区域
kernel = np.ones((50, 50), dtype=np.uint8)
dilate = cv.dilate(gray, kernel, 3)
cv.namedWindow("dilate",cv.WINDOW_NORMAL)
cv.imshow("dilate", dilate)
cv.waitKey(2000)
ret, mask_ = cv.threshold(dilate, 120, 255, cv.THRESH_BINARY_INV)#阈值1
cutImg = cv.bitwise_and(img, img, mask=mask_)
cv.namedWindow("cutImg",cv.WINDOW_NORMAL)
cv.imshow("cutImg", cutImg)
cv.waitKey(2000)

orange_lower = np.array([100, 43, 46])
orange_upper = np.array([124, 255, 255])  # 颜色色域
img_hsv = cv.cvtColor(cutImg, cv.COLOR_BGR2HSV)  # 转换为hsv
mask = cv.inRange(img_hsv, orange_lower, orange_upper)  # mask 启动
cv.namedWindow("mask",cv.WINDOW_NORMAL)
cv.imshow('mask', mask)
cv.waitKey(1000)
Ghost = cv.bitwise_and(gray, gray, mask=mask)
ret, mask1 = cv.threshold(Ghost, 5, 255, cv.THRESH_BINARY)#阈值2

#灰度值计算
Ghost_ = cv.bitwise_and(gray, gray, mask=mask1)
cv.namedWindow("ghost",cv.WINDOW_NORMAL)
cv.imshow("ghost", Ghost_)
cv.waitKey(1000)

row, col = Ghost_.shape
pixel_list = []
for i in range(row):
    for j in range(col):
        if Ghost_[i, j] != 0:
            x = Ghost_[i, j]
            pixel_list.append(x)
max = np.max(pixel_list)
mean = round(np.mean(pixel_list),2)
median = np.median(pixel_list)
print("max:" + str(max))
print("mean:" + str(mean))
print("median:" + str(median))

#三通道计算
Ghost_RGB = cv.bitwise_and(img,img,mask = mask1)
row_, col_ ,channel = Ghost_RGB.shape
R_Channel = 0
G_Channel = 0
B_Channel = 0
number = 0
for i in range(row_):
    for j in range(col_):
        if Ghost_RGB[i,j].any() != 0:
            number = number + 1
            B_Channel = B_Channel + Ghost_RGB[i,j,0]
            G_Channel = G_Channel + Ghost_RGB[i,j,1]
            R_Channel = R_Channel + Ghost_RGB[i,j,2]
print("pixel_number: " + str(number))
R_Channel_avg = round(R_Channel/number,2)
G_Channel_avg = round(G_Channel/number,2)
B_Channel_avg = round(B_Channel/number,2)
print("R_Channel_avg: " + str(R_Channel_avg))
print("R_Channel_avg: " + str(G_Channel_avg))
print("R_Channel_avg: " + str(B_Channel_avg))

'''
outPutData.write("max(weighted):"+str(max) + "\n")
outPutData.write("mean(weighted):"+str(mean) + "\n")
outPutData.write("median(weighted):"+str(median) + "\n")
outPutData.write("R_Channl_mean:"+str(R_Channel_avg) + "\n")
outPutData.write("G_Channel_mean:"+str(G_Channel_avg) + "\n")
outPutData.write("B_Channel_mean:"+str(B_Channel_avg) + "\n")
'''
plt.figure()
plt.subplot(221)
plt.imshow(img)
plt.subplot(222)
plt.imshow(dilate)
plt.subplot(223)
plt.imshow(mask)
plt.subplot(224)
plt.imshow(Ghost_)
#plt.text(-2000, 20,"mean:"+ str(mean),color = "r", size = 15, alpha = 0.2,bbox = dict(facecolor = "r", alpha = 0.2))
plt.ion()
plt.pause(10)

#plt.savefig(path + "\\Ghost_result\\" + dir)
# plt.savefig('D:\\python_practice\\导出的图片.png')
plt.close()




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


