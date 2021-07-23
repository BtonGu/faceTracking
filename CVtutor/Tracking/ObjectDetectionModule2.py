import cv2

def findObject(img,objectCascade,  scaleF =  1.1, minN = 4    ):
    
    imgObjects = img.copy()
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = objectCascade.detectMultiScale(imgGrey,   scaleF, minN  )
    objectsOut = []
    for(x,y,w,h) in objects:
        cv2.rectangle(imgObjects,(x,y),(x+w,y+h),(255,0,255),1)
        objectsOut.append( [ [x,y,w,h],w*h ])

    objectsOut = sorted( objectsOut , key = lambda x:x[1], reverse= True )    

    return imgObjects, objectsOut


def main():
    img = cv2.imread("../resource/aa.jpeg")
    faceCascade = cv2.CascadeClassifier("../resource/haarcascade_frontalface_default.xml")
    imgObjects, objects =  findObject(img , faceCascade)
    cv2.imshow("Output",imgObjects)
    cv2.waitKey(0)
    

if __name__== "__main__":
    main()

# import cv2
# img = cv2.imread("../resource/aa.jpeg")
# imgObjects = img.copy()
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

# faceCascade = cv2.CascadeClassifier("../resource/haarcascade_frontalface_default.xml")
# objects = faceCascade.detectMultiScale(  imgGrey, 1.1,4   )
# x,y,w,h = objects[0]

# cv2.rectangle(   imgObjects,(x,y), ((x+w),(y+h)),(255,0,0),2   )
# cv2.putText(imgObjects,  "face", (x,y) ,cv2.FONT_HERSHEY_DUPLEX,0.5, (0,250,0),1 )

# cv2.imshow("imgObjects",imgObjects)
# cv2.imshow("GRAY",imgGrey)
# cv2.waitKey(0)



