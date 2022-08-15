import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 
img_gray = cv.imread('Morphological Operation/abc.jpg',0)
img =  cv.imread('Morphological Operation/abc.jpg')
v,img_bw = cv.threshold(img_gray,160,255,cv.THRESH_BINARY_INV)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3)) #structuring element

img_erode = cv.morphologyEx(img_bw,cv.MORPH_ERODE,kernel,iterations=15)

plt.subplot(2,3,1),plt.imshow(img),plt.title('image'),plt.xticks([]),plt.yticks([])
plt.subplot(2,3,2),plt.imshow(img_erode,cmap='gray'),plt.title('erode'),plt.xticks([]),plt.yticks([])
plt.show()