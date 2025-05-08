# define a video capture object

import cv2
import time
num_frames=2
vid = cv2.VideoCapture(0)
ret, frame = vid.read()  
time.sleep(2)  
cv2.imshow('frame', frame)
for i in range (num_frames): 
  ret, frame = vid.read()  
  # Display the resulting frame
  cv2.imshow('frame', frame)
  time.sleep(1)
  cv2.imwrite('Leaf'+str(i)+'.jpg', frame)  
  time.sleep(1)
  

vid.release()

