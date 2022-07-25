import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Histogram/mark.jpg', 0)
threshold = int(input())
cv2.imshow('',img)
row, col = img.shape
for i in range(row):
  for j in range(col):
    if img[i,j] < threshold:
      img[i,j] = 0
    else:
      img[i,j] = 255
      
cv2.imshow('',img)
cv2.waitKey(0)