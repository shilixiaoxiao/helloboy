import numpy as np
import cv2

img = cv2.imread(r'D:\testFiles\pixel.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print
len(contours)
print
len(contours[0])
print
contours, '--------'
print
hierarchy, '********'
output = np.zeros(img.shape, dtype=np.uint8)
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)
cv2.imshow('whole', output)
cv2.waitKey(1000)
output[:] = 0

flag = [1, ] * len(contours)
for i in range(len(contours)):
    contour = contours[i].copy()
    index = i
    while flag[index] == 1:
        cv2.drawContours(output, [contour], -1, (0, 255, 0), 2)  # contours is a list
        flag[index] = 0
        print
        index
        index = hierarchy[0][index][0]  # dimension array
        cv2.imshow('stepbystep', output)
        cv2.waitKey(1000)
        if index == -1:
            print
            index
            break
        else:
            contour = contours[index]
