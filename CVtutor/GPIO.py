import Jetson.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while(True):
    GPIO.output(11,GPIO.HIGH)
    sleep(2)
    GPIO.output(11,GPIO.LOW)
    sleep(2)
GPIO.cleanup()


