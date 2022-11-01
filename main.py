# region IMPORTS
import serial
import time

# endregion

# region VARIABLES

divisions = 20 #parts per rotation
speed = 500 #mm/min
distance = 0.1 #mm per step
steps = 30 #steps per photo - *distance for total distance

# endregion

# region FUNCTIONS
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

# endregion

# region SETUP PRINTER

ser = serial.Serial('COM5', 115200)
arduino = serial.Serial(port='COM6', baudrate=115200, timeout=1)

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

# endregion

# region SETUP ARDUINO

# arduinoWrite(str(divisions))

# endregion

# region WAIT

input("Press to continue")

# endregion

# region RUN

print("Actual Run")

for i in range(divisions):
    for j in range(steps):
        arduinoWrite("Photo")
        command(ser, f"G0 Y{distance} F{speed}\r\n")
        time.sleep(1.5)

        print(f"Photo {j} of {steps}")
        print(f"Rotation {i} of {divisions}")
        print()

    arduinoWrite("Rotate")
    print("Rotate")
    time.sleep(1)

    command(ser, f"G0 Y-{distance * steps} F{speed}\r\n")
    time.sleep(2)


ser.close()

# endregion

# region REFERENCE

# G28 - Home
# G91 - Relative
# G0 - non-extrusion move

# endregion