import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('Histogram/v1.jpg', 0)
img2 = cv2.imread('Histogram/v2.jpg', 0)

hist1 = cv2.calcHist([img1], [0], None, [10], [0, 256])
h1, w1 = img1.shape
hist1n = hist1/(h1*w1)
hist2 = cv2.calcHist([img2], [0], None, [10], [0, 256])
h2, w2 = img2.shape
hist2n = hist2/(h2*w2)

diff = abs(hist1n - hist2n)

same = True
for d in diff:
    if d > 0.009:
        same = False
        break
# print(diff)
print(same)
if same is True:
    print("ภาพเหมือนกัน, มีผลต่างเท่ากับ =", diff)
else:
    print("ภาพต่างกัน, มีผลต่างเท่ากับ =", diff)
