import serial
import time

def arduinoWrite(x):
    arduino.write(str.encode(x))

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=1)
time.sleep(1)


while True:
    inp = input("Do : ")
    if(inp == "stop"):
        break
    else:
        arduinoWrite(inp)

arduino.close()