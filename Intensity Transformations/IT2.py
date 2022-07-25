import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = cv2.imread("low1.jpg",0)
[row,col] = img.shape
s1 = 50
r1 = 120
s2 = 220
r2 = 180

img1 = np.zeros((row,col),dtype='uint8')
for i in range(row):
  for j in range(col):
    if img[i,j]>=0 and img[i,j]<r1:
      img1[i,j] = np.array((s1/r1)*img[i,j],dtype='uint8')
    if img[i,j]>=r1 and img[i,j]<r2:
      img1[i,j] = np.array((((s2-s1)/(r2-r1)))*(img[i,j]-r1)+s1,dtype='uint8')
    if img[i,j] >= r2 and img[i,j] <=255:
      img1[i,j] = np.array((((255-s2)/(255-r2)))*(img[i,j]-r2)+s2,dtype='uint8')

modifly_img = cv2.hconcat([img,img1])
cv2.imshow('',modifly_img)
cv2.waitKey(0)