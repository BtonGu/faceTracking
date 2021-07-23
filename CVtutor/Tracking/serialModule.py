from os import write
import serial
#sudo chmod 666 /dev/ttyACM0
#  ls /dev/ttyACM*


def initConnetion(portNo,baudRate):
    try:
           ser = serial.Serial(portNo,baudRate)
           print ("Device Connected")
           return ser
    except:
        print("Not Connected")

  #十六进制的发送
def  transmitt(ser,num):
    result=ser.write(chr(num).encode("utf-8"))#写数据
    print("发送:",num)

if __name__== "__main__":
    ser = initConnetion('/dev/ttyACM0',  115200 )
    transmitt(ser,0x0a)

# try:
#     ser = serial.Serial("/dev/ttyACM0", 115200)
#     print("Device Connected")
#     result=ser.write(   chr(0x10).encode("utf-8")       )
#     print("OK?",result)
#     result=ser.write(   ("hello").encode("utf-8")       )
#     print("OK?",result)

# except:
#     print("Not Connected")




