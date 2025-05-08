import cv2
import time
#camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera = cv2.VideoCapture(1)

for i in range(10):
    return_value, image = camera.read()
    cv2.imshow('image', image) 
    cv2.imwrite('sakthi'+str(i)+'.jpg', image)
    time.sleep(2)



