from sys import flags
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('in_class/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('in_class/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('in_class/haarcascade_mcs_mouth')


cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray,2)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray,2)
        for (x, y, w, h) in eyes:
            cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)
            break

    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        break
    cv2.putText(img,'Mask  '+str(len(eyes)/2) + '    No mask  ' + str(len(faces)), (25, 25),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    
    
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
