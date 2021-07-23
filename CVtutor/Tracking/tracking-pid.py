#from typing import no_type_check
import cv2
import ObjectDetectionModule2 as odm
import serialModule as sm
import numpy as np 
import maskModule as msk 

frameWidth =640
frameHeight = 480

flip=0

camSet = 1 #usb

cap = cv2.VideoCapture(camSet, cv2.CAP_GSTREAMER)  #cap = cv2.VideoCapture(camSet)
ser = sm.initConnetion('/dev/ttyACM0',  115200 )
sm.transmitt(ser,0x96)
#sudo chmod 666 /dev/ttyACM0
faceCascade = cv2.CascadeClassifier("../resource/haarcascade_frontalface_default.xml")
mask = cv2.imread('../resource/glass.jpeg')

def findCenter(imgObjects, objects):
    cx, cy = -1,-1
    if len(objects)!=0 :
        x,y,w,h = objects[0][ 0 ]
        cx= x +w/2
        cy= y+ h/2
        cx,cy=int(cx), int(cy)
        cv2.circle(imgObjects,  ((cx),(cy)),2,(0,255,0),cv2.FILLED)
        ih,iw,ic =imgObjects.shape
        cv2.line(imgObjects,  (iw//2,cy),  (cx,cy),   (0,255,0), 1)
        cv2.line(imgObjects,  (cx,ih//2),  (cx,cy),   (0,255,0), 1)
    return (cx),(cy),imgObjects

perrorLR,perrorUD,posX=0,0,0x96

def trackObjects(cx,cy,w,h):

    global perrorLR,perrorUD,posX
    kLR = [0.07,0.04]
    kUD= [0.5,0.5]

    #left or right
    if  cx!=-1:
        errorLR= w//2 -cx
        print("errorLR=",errorLR)
        posX += kLR[0]*errorLR + kLR[1] *(errorLR-perrorLR)
        posX = int(posX)
        perrorLR = errorLR

        if posX>250:posX=250
        if posX< 51  :posX=51

        sm.transmitt(ser,   posX )   

     
while True:
    success,img = cap.read()
    img = cv2.resize(img,(0,0),None,0.3,0.3)
    imgObjects,objects = odm.findObject(img,faceCascade)
    imgObjects = msk.Mask(imgObjects,objects,mask)
    cx,cy,imgObjects = findCenter(imgObjects,objects)
    

    h,w,c = imgObjects.shape
    cv2.line( imgObjects,     (w//2,0),(w//2,h),(255,180,10),1   )
    cv2.line(  imgObjects,    (0,h//2), (w,h//2),(255,180,10),1   )

    trackObjects(cx,cy,w,h)

    img = cv2.resize(imgObjects,(0,0),None,4,4)
    cv2.imshow("Image",img)
    if cv2.waitKey(1)  & 0xff == ord('q') :
        sm.transmitt(ser,0x33)
        break

    