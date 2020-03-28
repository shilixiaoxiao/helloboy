# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

Img = np.zeros((1600, 1600), dtype=np.uint8)
Img.fill(255)
Img = cv.cvtColor(Img, cv.COLOR_GRAY2BGR)
h = Img.shape[0]
w = Img.shape[1]
print(w,h)

cv.line(Img, (0, int(h / 2)), (w-1, int(h / 2)), (0, 0, 255), thickness=2, lineType=8, shift=0)
cv.line(Img, (int(w / 2), 0), (int(w / 2), h-1), (0, 0, 255), thickness=2, lineType=8, shift=0)
cv.line(Img, (0, 0), (0, h-1), (0, 0, 255), thickness=2, lineType=8, shift=0)
cv.line(Img, (0, 0), (w-1, 0), (0, 0, 255), thickness=2, lineType=8, shift=0)
cv.line(Img, (0, h-1), (w-1, h-1), (0, 0, 255), thickness=2, lineType=8, shift=0)
cv.line(Img, (w-1, 0), (w-1, h-1), (0, 0, 255), thickness=2, lineType=8, shift=0)
cv.imshow("IMG",Img)
cv.waitKey(1000)
cv.imwrite(r"crossLine.bmp", Img)

