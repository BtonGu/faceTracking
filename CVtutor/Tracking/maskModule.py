
import numpy as np
import cv2
import ObjectDetectionModule2 as odm
 
# face_detector = cv2.CascadeClassifier('../resource/haarcascade_frontalface_default.xml')
# video = cv2.VideoCapture(1)#打开电脑上的摄像头
# mask = cv2.imread('../resource/glass.jpeg')#读取文件，速度慢


# while True:
#     flag,frame = video.read()
#     if flag == False:
#         break
#     gray = cv2.cvtColor(frame,code = cv2.COLOR_BGR2GRAY)
#     face_zones = face_detector.detectMultiScale(gray)
#     mask2 = mask.copy()#快
#     for x,y,w,h in face_zones:
#         mask2 = cv2.resize(mask2,(w,h))
#        #frame[y:y+h,x:x+w] = mask2
#         for i in range(h):#高度 y
#              for j in range(w):#宽度 x
#                 b,g,r = mask2[i,j]
#                 if (b<180)&(g<180)&(r<180):
#                     frame[y+i-10,x+j] = mask2[i,j]
#     cv2.imshow('ttnk',frame)
#     key = cv2.waitKey(41)
#     if key == ord('q'):#退出条件
#         break
# cv2.destroyAllWindows()
# video.release()


# cv2.imshow("ING",mask)
# cv2.waitKey(0)

def Mask(imgObjects,objects,mask):
    if len(objects)!=0 :
        mask2 = mask.copy()#快
        x,y,w,h = objects[0][0]
        mask2 = cv2.resize(mask2,(w,h))
        #frame[y:y+h,x:x+w] = mask2
        for i in range(h):#高度 y
            for j in range(w):#宽度 x
                b,g,r = mask2[i,j]
                if (b<180)&(g<180)&(r<180):
                    imgObjects[y+i-2,x+j] = mask2[i,j]
    return imgObjects




def main():
    faceCascade = cv2.CascadeClassifier('../resource/haarcascade_frontalface_default.xml')
    video = cv2.VideoCapture(1)#打开电脑上的摄像头
    mask = cv2.imread('../resource/glass.jpeg')#读取文件，速度慢

    while True:
        flag,imgObjects = video.read()
        if flag == False:
            break
        imgObjects = cv2.resize(imgObjects,(0,0),None,0.3,0.3)
        imgObjects,objects = odm.findObject(imgObjects,faceCascade)

        imgObjects = Mask(imgObjects,objects,mask)

        imgObjects = cv2.resize(imgObjects,(0,0),None,3,3)
        cv2.imshow('ttnk',imgObjects)
        key = cv2.waitKey(41)
        if key == ord('q'):#退出条件
            break
    cv2.destroyAllWindows()
    video.release()
    
    

if __name__== "__main__":
    main()