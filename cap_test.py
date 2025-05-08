import cv2
vid = cv2.VideoCapture(0)
i=0  
while(True):  
    ret, frame = vid.read()  
    cv2.imshow('frame', frame)      
    
     
    if cv2.waitKey(1) & 0xFF == ord('s'):
          i=i+1
          try:                
            cv2.imwrite('Leaf'+str(i)+'.jpg', frame)
            print(str(1)+"--image saved")    
          except:
            print("Save error")
              
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting")        
        break
  

vid.release()

cv2.destroyAllWindows()
