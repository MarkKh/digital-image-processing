import numpy as np
import cv2
img = cv2.imread('/content/chest_xray1.jpg')

print('เลือก 1 หรือ 2\n1.เพิ่มความสว่าง\n2.ลดความสว่าง')
inp = int(input())

if inp == 1:
  lev = input('เลือกระดับความสว่าง น้อย ปานกลาง หรือมาก : ')
  if lev == 'น้อย':
    gm = np.array(255*(img/255)**0.67,dtype='uint8')
  elif lev == 'ปานกลาง':
    gm = np.array(255*(img/255)**0.2,dtype='uint8')
  elif lev == 'มาก':
    gm = np.array(255*(img/255)**0.04,dtype='uint8')

elif inp == 2:
  lev = input('เลือกระดับความสว่าง น้อย ปานกลาง หรือมาก : ')
  if lev == 'น้อย':
    gm = np.array(255*(img/255)**1.5,dtype='uint8')
  elif lev == 'ปานกลาง':
    gm = np.array(255*(img/255)**5,dtype='uint8')
  elif lev == 'มาก':
    gm = np.array(255*(img/255)**25,dtype='uint8')

modifly_img = cv2.hconcat([img,gm])
cv2.imshow('',modifly_img)