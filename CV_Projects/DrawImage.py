# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

r = 640
c = 360
for k in range(3):
    for h in range(3):
        Img = np.zeros((1080, 1920), dtype=np.uint8)
        Img = cv.cvtColor(Img, cv.COLOR_GRAY2BGR)
        for i in range(r):
            for j in range(c):
                #Img[8*j,8*i] = (255,255,255)
                #Img[8*j+h,8*i] = (255,255,255)
                #Img[8*j,8*i+k] = (255,255,255)
                Img[3*j+h,3*i+k] = (0,255,0)
        #cv.imshow("IMG",Img)
        #cv.waitKey(1000)
        cv.imwrite(r"D:\dot_" + str((k,h)) + ".png",Img)
