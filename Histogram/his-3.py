import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Histogram/mark.jpg', 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

bright = sum(hist[170:255])
dark = sum(hist[0:84])
low = sum(hist[85:169])
if bright > dark and bright > low:
    print("Bright Image")
elif dark > low:
    print("Dark Image")
else:
    print("Low Contrast")

cv2.imshow('',img)
cv2.waitKey(0)
