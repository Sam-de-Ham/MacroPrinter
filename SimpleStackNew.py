#Imports
import serial
import time


#Variables
speed = 500 #mm/min
distance = 0.05 #mm per step
steps = 100 #steps per photo - *distance for total distance

#functions
def command(ser, command):
    ser.write(str.encode(command))
    time.sleep(1)

    while True:
        line = ser.readline()
        # print("Read :", line)
        if line == b'ok 0\r\n':
            break
def arduinoWrite(x):
    arduino.write(str.encode(x))


#setup
ser = serial.Serial('COM6', 115200)
arduino = serial.Serial(port='COM10', baudrate=115200, timeout=1)


#homing
time.sleep(3)

command(ser, "G28\r\n")
time.sleep(5)
print("Home finished")

command(ser, "G91\r\n")
print("Relative")

command(ser, "G0 Y150\r\n")
print("Moved Forward")

time.sleep(2)

command(ser, "G0 Z60\r\n")
print("Moved Up")

time.sleep(2)


#wait for user
input("Press to continue")


#run
print("\nActual Run\n")

for j in range(steps):
    arduinoWrite("Photo")
    command(ser, f"G0 Y{distance} F{speed}\r\n")
    time.sleep(1.5)

    print(f"Photo {j} of {steps}")
    print()


#finish
command(ser, f"G0 Y{-distance*steps} F{speed}\r\n")

ser.close()
print("FINISHED")
