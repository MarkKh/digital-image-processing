import cv2 as cv
import numpy as np

image = cv.imread('MiniTest/E2.jpg')
img = cv.resize(image, None, fx=0.5, fy=0.5)
imgBlur = cv.medianBlur(img, 25)

hsv = cv.cvtColor(imgBlur, cv.COLOR_BGR2HSV)

red1 = np.array([0, 0, 210])
red2 = np.array([200, 255, 255])

mark = cv.inRange(hsv, red1, red2)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (11, 11))
khom = cv.morphologyEx(mark, cv.MORPH_OPEN, kernel, iterations=1)
dilate = cv.morphologyEx(khom, cv.MORPH_CLOSE, kernel, iterations=1)
contours, h = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

for i in contours:
    cv.drawContours(img, i, -1, (0, 255, 0), 3)

cv.imshow("Tomato detection", img)
print("Tomato = " + str(len(contours)))
cv.waitKey(0)
cv.destroyAllWindows()
