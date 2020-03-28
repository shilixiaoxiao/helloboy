import cv2 as cv
import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
import re

path = "D:\\testFiles\\BrightCircle\\"
listDir = os.listdir(path)
print(listDir)

outPutData = open(path + "\\" + "BC.txt",'w')

for dir in listDir:
    if re.match('IMG_00'+r'\d+',dir):
        print(path +"\\"+ dir)
        outPutData.write( dir + ":\n")
        inputImg = cv.imread(path + "\\" + dir)
        #print(inputImg)