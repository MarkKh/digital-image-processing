import cv2
import numpy as np

img = cv2.imread("Colorimageprocessing/lemon.jpg")
height, width, channels = img.shape
def contains_colors(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    p = cv2.inRange(hsv, (22,93,0), (45, 255, 255))
    ones1 = cv2.countNonZero(p)
    percent_color1 = (ones1/(height*width)) * 100
    mask2 = cv2.inRange(hsv, (25, 52, 72), (102, 255,255))
    ones2 = cv2.countNonZero(mask2)
    percent_color2 = (ones2/(height*width)) * 100
    if percent_color1 > percent_color2:
        return 1
    else:
        return 255
if contains_colors(img) == True:
    print("Lemon")
else:
    print("Lime")