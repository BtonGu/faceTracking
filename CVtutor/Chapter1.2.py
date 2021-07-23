 #_, frame = cam.read()
# img = cv2.imread("resource/aa.jpeg")
# cap = cv2.VideoCapture("resource/car.mp4")
#cam = cv2.VideoCapture('/dev/video2')
# camSet = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=2 ! video/x-raw, width=640, height=480, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

''''''
#gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=3820, height=2464, framerate=21/1, format=NV12' ! nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=616' ! nvvidconv ! nvegltransform ! nveglglessink -e
#v4l2-ctl --list-device
''''''

# run webcam
import cv2
frameWidth = 640
frameHeight=480
flip=0
CSIcamSet = ('nvarguscamerasrc ! '
                   'video/x-raw(memory:NVMM), '
                   'width=(int)1920, height=(int)1080, '
                   'format=(string)NV12, framerate=(fraction)21/1 ! '
                   'nvvidconv flip-method='+str(flip)+' ! '
                   'video/x-raw, width=(int){}, height=(int){}, '
                   'format=(string)BGRx ! '
                   'videoconvert ! appsink').format(frameWidth, frameHeight)
USBcamera=1
Video = "resource/car.mp4"


cap = cv2.VideoCapture( Video ) 
while True:
    success,img = cap.read()
    img = cv2.imread("resource/aa.jpeg")
    cv2.imshow('Ruselt', img )
    if cv2.waitKey(1)  &  0xff  == ord('q'):
        break




