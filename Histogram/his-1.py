import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Histogram/mark.jpg',0)

inp = int(input('brightness(0 - 256) = '))

plt.hist(img.ravel(),inp,[0,256]); 
plt.show()