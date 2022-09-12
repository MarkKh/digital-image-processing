import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imgcolor=cv.imread('FeatureExtraction/t1.jpg')   
imgcolor = cv.cvtColor(imgcolor, cv.COLOR_BGR2RGB)
img = cv.imread('FeatureExtraction/t1.jpg',0)
template_color = cv.imread('FeatureExtraction/t1_1.png')  
template_color = cv.cvtColor(template_color, cv.COLOR_BGR2RGB)
template = cv.imread('FeatureExtraction/t1_1.png',0)
h, w = template.shape

# Apply template Matching
res = cv.matchTemplate(img,template,cv.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
top_left = min_loc
# Other method
#top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(imgcolor,top_left, bottom_right, (0,255,0), 2)
plt.subplot(1,3,1),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(template_color)
plt.title('Template'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(imgcolor)
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()