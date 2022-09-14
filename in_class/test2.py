import cv2

face_cascade = cv2.CascadeClassifier('in_class/haarcascade_frontalface_default.xml')
Mouth_cascade = cv2.CascadeClassifier('in_class/haarcascade_mcs_mouth.xml')
eyes_cascade = cv2.CascadeClassifier('in_class/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
PWM = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame,1.3,5)
    mouth = Mouth_cascade.detectMultiScale(frame,1.3,5)
    eyes = eyes_cascade.detectMultiScale(frame,1.3,5)


    for (x,y,w, h) in eyes:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)

    
    cv2.imshow('CamShow',gray) 
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()