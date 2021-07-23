import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img[:] = 255,255,255

cv2.circle(img, (256,256),150,(0,69,0)   ,cv2.FILLED)
#cv2.cicle( img, center, radius,color, thickness)
cv2.rectangle(img,(130,226),(382,286),     (255,255,255),cv2.FILLED)
#cv2.rectangle(img,pt1,pt2, color,thickness)
cv2.line(img,(130,296),(382,296)    ,(255,255,255),2)

cv2.putText(img,  "Hello G" ,     (137,262), cv2.FONT_HERSHEY_DUPLEX,1.5,(0,69,255),2)

cv2.imshow("Image",img)
cv2.waitKey(0)