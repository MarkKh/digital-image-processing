import cv2 as cv
import numpy as np
# Loads an image

img = cv.imread('Segmentation/testcolor.jpg')
src1 = cv.resize(img , None , fx=0.3 , fy=0.3)
src2 = cv.resize(img , None , fx=0.3 , fy=0.3)
src = cv.resize(img , None , fx=0.3 , fy=0.3)
imgBlur = cv.medianBlur(src, 5)

hsv = cv.cvtColor(imgBlur, cv.COLOR_BGR2HSV)
cv.imshow("src", src)
lower_green1 = np.array([35, 52, 72])   # (38, 86, 0)
upper_green1 = np.array([102, 255, 255])   # (121, 255, 255)
lower_green2 = np.array([20, 50, 50])   # (38, 86, 0)
upper_green2 = np.array([43, 255, 255])   # (121, 255, 255)

markkh = cv.inRange(hsv, lower_green1 , upper_green1)
sea_tawinan = cv.inRange(hsv, lower_green2 , upper_green2)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(11,11))
dilate1 = cv.dilate(markkh,kernel,iterations = 1)
dilate2 = cv.dilate(sea_tawinan,kernel,iterations = 1)
cv.imshow("test1", dilate1)
cv.imshow("test2", markkh)
contours1,h = cv.findContours(dilate1, cv.RETR_EXTERNAL , cv.CHAIN_APPROX_NONE)
contours2,h = cv.findContours(dilate2, cv.RETR_EXTERNAL , cv.CHAIN_APPROX_NONE)
for fforce_ in contours1:
        cv.drawContours(src1, fforce_, -1, (0, 255, 0), 3)

for kasibook_ in contours2:
        cv.drawContours(src2, kasibook_, -1, (0, 255, 0), 3)

cv.imshow("Object detection1", src1)
cv.imshow("Object detection2", src2)
print("จำนวนมะนาวเขียว = " + str(len(contours1)))
print("จำนวนมะนาวเหลือง = " + str(len(contours2)-len(contours1)))
print("จำนวนมะนาวทั้งหมด = " + str(len(contours2)))

cv.waitKey(0)
cv.destroyAllWindows()