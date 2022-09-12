import sys
import cv2 as cv
import numpy as np

default_file = ('FeatureExtraction/testcolor.jpg')
# Loads an image
src = cv.imread(default_file)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 9)
rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 9, param1=190, param2=20,minRadius=50, maxRadius=480)
print(circles[0:])

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(src, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv.circle(src, center, radius, (255, 0, 255), 3)
print(" จำนวนลูก :"+str(len(circles[0,:])))
cv.imshow('',src)
cv.waitKey(0)