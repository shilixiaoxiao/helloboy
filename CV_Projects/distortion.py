# -*- coding: utf-8 -*-

from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"D:\IMG_0261.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,127,255,0)
contours, hieratchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),3)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img",img)
cv2.waitKey(0)

'''# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]

cv2.namedWindow('dst',cv2.WINDOW_NORMAL)
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
'''

'''# 读取图片
image = cv2.imread(r"D:\IMG_0261.jpg")
# 执行灰度变换
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
image[dst>0.01*dst.max()]=[0,0,255]

cv2.namedWindow('dst',cv2.WINDOW_NORMAL)
cv2.imshow('dst',image)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()'''

'''# 执行高斯滤波
#gray = cv2.GaussianBlur(gray, (7, 7), 0)

dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
print(ret)
# print(labels)
# print(labels[2])
print(stats.shape)
# print(centroids)

#定义停止和细化角点的标准
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
ret, dst = cv.threshold(dst, 0.01*dst.max(), 255, cv.THRESH_BINARY)
dst = np.uint8(dst)
cv.imwrite('img/thresh3.png', dst)

ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

corners = cv.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
'''

'''# 执行Canny边缘检测
edged = cv2.Canny(gray, 5, 100)
cv2.namedWindow("edged",cv2.WINDOW_NORMAL)
cv2.imshow("edged",edged)
cv2.waitKey(4000)
# 执行腐蚀和膨胀后处理
#edged = cv2.dilate(edged, None, iterations=1)
#edged = cv2.erode(edged, None, iterations=1)

# 在边缘映射中寻找轮廓
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
'''