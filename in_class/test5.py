import cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('in_class/haarcascade_frontalface_default.xml')
# เชื่อมต่อ default camera ระบุเลข 0
mouth_cascade = cv2.CascadeClassifier('in_class/haarcascade_mcs_mouth')
eye_cascade = cv2.CascadeClassifier('in_class/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
# ใช้ ขนาด width x height แบบอัตโนมัติ
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:

    # Capture frame-by-frame

    ret, frame = cap.read()

    # คำสั่งนี้ทำให้ VDO เป็น gray scale ถ้าอยากได้เป็นภาพสี ก็ทำ Comment ออก

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    eyes = eye_cascade.detectMultiScale(gray,2,5)
    mouth = mouth_cascade.detectMultiScale(gray,1.3,5)
    
    for (ex,ey,ew,eh) in eyes :
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),4)

    for (mx,my,mw,mh) in mouth:
        cv2.rectangle(frame,(mx,my),(mx+mw,my+mh),(0,0,255),2)

        break

    mask = "No mask "+str(len(mouth))+"   "+"Mask"+str((len(eyes)//2)-len(mouth))

    cv2.putText(frame, mask, (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('img',frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()
