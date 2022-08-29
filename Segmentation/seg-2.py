import cv2 as cv
import numpy as np

# Loads an image
src = cv.imread('Segmentation/testcolor.jpg')
src1 =cv.resize(src , None , fx=0.3 , fy=0.3)
src2 =cv.resize(src , None , fx=0.3 , fy=0.3)
src3 =cv.resize(src , None , fx=0.3 , fy=0.3)
src4 =cv.resize(src , None , fx=0.3 , fy=0.3)
src =cv.resize(src , None , fx=0.3 , fy=0.3)

imgBlur = cv.medianBlur(src, 11)

####### convert to grayscale (gray scale) #########
Gray = cv.cvtColor(imgBlur, cv.COLOR_BGR2GRAY)

###### convert to black and white #####
ret3,th3 = cv.threshold(Gray,90,255,cv.THRESH_BINARY)

####### Convert to HSV color #########
hsv = cv.cvtColor(imgBlur, cv.COLOR_BGR2HSV)
lower_green = np.array([30, 50, 50])
upper_green = np.array([60, 255, 255])
lower_yellow = np.array([20,100,100])
upper_yellow = np.array([30,255,255])  #[27,255,255]

###### Finds pixels in an image with a given hsv color gamut. ###### หาพิกเซลในรูปที่มี ช่วงสี hsv ที่กำหนด
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(11,11))
##### Yellow Color ####
mask_yellow = cv.inRange(hsv, lower_yellow , upper_yellow)
opening_yellow = cv.morphologyEx(mask_yellow, cv.MORPH_OPEN, kernel, iterations = 1)
closed_yellow = cv.morphologyEx(opening_yellow, cv.MORPH_CLOSE, kernel, iterations = 1)

##### Green Color ####
mask_green = cv.inRange(hsv, lower_green , upper_green)
opening_green = cv.morphologyEx(mask_green, cv.MORPH_OPEN, kernel, iterations = 1)
closed_green = cv.morphologyEx(opening_green, cv.MORPH_CLOSE, kernel, iterations = 1)

fforce_,h = cv.findContours(closed_green, cv.RETR_EXTERNAL , cv.CHAIN_APPROX_NONE)
kasibook_,h = cv.findContours(closed_yellow, cv.RETR_EXTERNAL , cv.CHAIN_APPROX_NONE)

#Crete variable count lemon
small_green_lemon = 0
big_green_lemon = 0
small_yellow_lemon = 0
big_yellow_lemon = 0
for ppromxx_ in fforce_:
        pr= cv.arcLength(ppromxx_,True)
        M = cv.moments(ppromxx_)
        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        if pr < 250 :   
            small_green_lemon=small_green_lemon+1
            cv.drawContours(src1, ppromxx_, -1, (0, 255, 0), 3)
            
        else :
            big_green_lemon=big_green_lemon+1
            cv.drawContours(src2, ppromxx_, -1, (255, 0, 0), 3)
           
for louis in kasibook_:
        pr= cv.arcLength(louis,True)
        M = cv.moments(louis)
        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        if pr < 250 :
            small_yellow_lemon=small_yellow_lemon+1
            cv.drawContours(src3, louis, -1, (0, 255, 0), 3)
        else :
            big_yellow_lemon=big_yellow_lemon+1
            cv.drawContours(src4, louis, -1, (255, 0, 0), 3)

cv.imshow("G(S)", src1)
cv.imshow("G(L)", src2)
cv.imshow("Y(S)", src3)
cv.imshow("Y(L)", src4)

print("G(S) = " , small_green_lemon)
print("G(L) = " , big_green_lemon)
print("Y(S) = " , small_yellow_lemon)
print("Y(L) = " , big_yellow_lemon)

print("Total number of green lemons = " + str(len(fforce_)))
print("Total number of yellow lemons = " + str(len(kasibook_)))
cv.waitKey(0)
cv.destroyAllWindows()