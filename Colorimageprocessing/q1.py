import cv2
import numpy as np

image = cv2.imread('Colorimageprocessing/chest_xray1.jpg',
                   cv2.IMREAD_GRAYSCALE)
image_resize = cv2.resize(image, (400, 400))
color_amount = int(input('จำนวนสีที่ต้องการ (ไม่เกิน 5 สี) : '))
row, column = image_resize.shape

# empty array to store image.
sliced_image = np.zeros((row, column, 3), dtype='uint8')

colors = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [0, 255, 255]
]

color_range = np.array_split(np.array(range(0, 256)), color_amount)

for i in range(row):
    for j in range(column):
        ct = 0
        for k in color_range:
            if image_resize[i, j] in k:
                sliced_image[i, j] = colors[ct]
            ct += 1

cv2.imshow('', sliced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
