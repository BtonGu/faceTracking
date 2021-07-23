import cv2
import numpy as np
img = cv2. imread("./resource/aa.jpeg")
imgGrey =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, ( 3,3 ) , 3)
imgCannay = cv2.Canny(imgBlur,100,150)
kernel = np.ones((3,3),"uint8")
imgDia = cv2.dilate(imgCannay,kernel,iterations=1)
imgErode = cv2.erode(imgDia,kernel,iterations=1)


cv2.imshow("Image_Grey",imgGrey)
cv2.imshow("Image_Blur",imgBlur)
cv2.imshow("Image_canny",imgCannay)
cv2.imshow("Image_Dia",imgDia)
cv2.imshow("Image_Erode",imgErode)
cv2.waitKey(0)