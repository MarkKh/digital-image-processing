import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('Histogram/mark.jpg', 0)

dim = image.size

plt.hist(image.ravel()/dim)
plt.show()