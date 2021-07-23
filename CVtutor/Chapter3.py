import cv2
import numpy as np


img = cv2.imread("./resource/aa.jpeg")
print(img.shape)

imgResize = cv2.resize(img,(640,460))
imgResize2 = cv2.resize(img,(0,0),None,0.5,0.5)
print(imgResize2.shape)

imgCrop = img[100:200,200:300]


cv2.imshow("Image",img)
cv2.imshow("ImageRZ",imgResize)
cv2.imshow("ImageRZ2",imgResize2)
cv2.imshow("imgCrop",imgCrop)
cv2.waitKey(0)