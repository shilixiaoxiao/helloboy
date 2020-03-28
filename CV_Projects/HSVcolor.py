import cv2
import numpy as np

'''cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()'''

img = cv2.imread(r"D:\testFiles\pixel.jpg")
#cv2.imshow("img",img)
#cv2.waitKey(1000)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 在HSV空间中定义绿色
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green) #lower20===>0,upper200==>0,

green_res = cv2.bitwise_and(img, img, mask = mask)

#部分5:将BGR空间下的图片转换成RGB空间下的图片
#img = img[:,:,::-1]
#green_res = green_res[:,:,::-1]
cv2.imshow("green",green_res)
cv2.waitKey(1000)

gray = cv2.cvtColor(green_res,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(1000)
cv2.imwrite(r"D:\testFiles\gray.jpg",gray)
ret, binary = cv2.threshold(gray,90,255,cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel,iterations=3)
canny_output = cv2.Canny(binary,50,150)
cv2.imshow("canny",canny_output)
cv2.waitKey(1000)
contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
number = np.shape(contours)[0]
print(number)
for i in range(number):
    cv2.drawContours(img,contours,-1,(0,0,255),3)
cv2.imshow("img",img)
cv2.waitKey(30000)
#cv2.imshow("binary",binary)
#cv2.waitKey(1000)

'''edge_output = cv2.Canny(gray, 50, 150) 
   cv2.imshow("edge_output",edge_output)
   cv2.waitKey(1000)'''

'''contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
number = np.shape(contours)[0]
print(number)'''


"""for i in range(number):
    cv2.drawContours(img,contours,-1,(0,0,255),3)
cv2.imshow("img",img)
cv2.waitKey(1000)"""




'''import cv2
import numpy as np
img = cv2.imread('IMG_0307.jpg')
orange_lower = np.array([11,43,46])
orange_upper = np.array([25,255,255]) #颜色色域
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #注意 一定要转换为hsv 
mask = cv2.inRange(img_hsv,orange_lower,orange_upper) #mask 启动
mask = cv2.erode(mask,None,iterations=2) 
mask = cv2.GaussianBlur(mask,(3,3),0)
#erode 和 GaussianBlur 是用来使得图片或视频更加模糊的 这样可以使得色彩突出更加明显，#色彩追踪也会更加精准
cv2.imshow('mask',mask)
cv2.imshow('img',img)
cv2.waitKey()
'''