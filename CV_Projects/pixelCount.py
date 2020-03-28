# -*- coding: utf-8 -*-
import cv2
import numpy as np


img = cv2.imread(r"D:\testFiles\dot_(0, 0).png",0)
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#使用局部阈值的大津算法进行图像二值化
dst = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,101, 1)

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3, 3))#形态学去噪
dst=cv2.morphologyEx(dst,cv2.MORPH_OPEN,element)  #开运算去噪
ret,dst=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  #轮廓检测函数
cv2.drawContours(dst,contours,-1,(120,0,0),2)  #绘制轮廓

count=0 #米粒总数
ares_avrg=0  #米粒平均
#遍历找到的所有米粒
for cont in contours:

    ares = cv2.contourArea(cont)#计算包围性状的面积

    if ares<50:   #过滤面积小于10的形状
        continue
    count+=1    #总体计数加1
    ares_avrg+=ares

    print("{}-blob:{}".format(count,ares),end="  ") #打印出每个米粒的面积

    rect = cv2.boundingRect(cont) #提取矩形坐标

    print("x:{} y:{}".format(rect[0],rect[1]))#打印坐标

    cv2.rectangle(img,rect,(0,0,0xff),1)#绘制矩形

    y=10 if rect[1]<10 else rect[1] #防止编号到图片之外

    cv2.putText(img,str(count), (rect[0], y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1) #在米粒左上角写上编号

print("米粒平均面积:{}".format(round(ares_avrg/ares,2))) #打印出每个米粒的面积

"""cv2.findContours()
cv2.boundingRect()
cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
cv2.putText(img,str(count), (rect[0], y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
ares = cv2.contourArea(cont)"""


'''Img = cv.imread(r"D:\IMG_0125.jpg",0)
cv.namedWindow('input_image',cv.WINDOW_NORMAL)
cv.imshow("input_image",Img)
cv.waitKey(1000)
ImgGray = cv.cvtColor(Img, cv.COLOR_BGR2GRAY)
#cv.imshow("IMGGRAY",ImgGray)
#print(ImgGray)
#cv.waitKey(3000)

ret, binary = cv.threshold(ImgGray,100,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("binary image", binary)
cloneTmage, contours, heriachy = cv.findContours(Img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for i, contour in enumerate(contours):
        cv.drawContours(Img, contours, i, (0, 0, 255), 2)
        print(i)
cv.imshow("contours", Img)
len(contours)
for i, contour in enumerate(contours):
        cv.drawContours(Img, contours, i, (0, 0, 255), -1)
        cv.imshow("pcontours", Img)
src = cv.imread('E:/imageload/coins.jpg')
cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()'''



"""
#Binarization = cv.cvtColor(th3,cv.COLOR_GRAY2BGR)
#h = Binarization.shape[0]
#w = Binarization.shape[1]
h, w = th3.shape[:2]
cv.imshow("th3",Binarization)
print(th3)

number = 0
for i in range(h):
    for j in range(w):
        if th3[i,j] == 255:
            number += 1
print(number)
"""
