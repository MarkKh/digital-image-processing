import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('MiniTest/E1.png')
# 1.1 Show image shape
print('1.1', image.shape)

# 1.1 ย่อขนาดภาพลง 30%
resizeImage = cv2.resize(image, None, fx=0.7, fy=0.7)
print('1.2', resizeImage.shape)
cv2.imshow('1.2', resizeImage)

# 1.3 convert to สีตรงข้าม
convertImage = cv2.cvtColor(resizeImage, cv2.COLOR_BGR2RGB)
cv2.imshow('1.3', convertImage)

# 1.5 convert to gray
gray = cv2.cvtColor(resizeImage, cv2.COLOR_BGR2GRAY)
cv2.imshow('1.5', gray)

# 1.4 histogram
plt.hist(resizeImage.ravel(), 256, [0, 32])
plt.show()

cv2.waitKey(0)
