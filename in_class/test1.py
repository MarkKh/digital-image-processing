import cv2

face_cascade = cv2.CascadeClassifier('in_class/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame,1.3,5)

    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 255), 2)
        cv2.putText(gray,'Face',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0, 255), 2)
    
    cv2.imshow('CamShow',gray) 
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()