# region IMPORTS
import serial
import time

# endregion

# region VARIABLES

divisions = 100 #parts per rotation

# endregion

# region FUNCTIONS
def arduinoWrite(x):
    arduino.write(str.encode(x))

# endregion

# region CREATE ARDUINO

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=1)
time.sleep(3)

# endregion

# region RUN

print("Actual Run")

for i in range(divisions):
    print(f"Photo {i+1} of {divisions}")
    arduinoWrite("Photo")
    time.sleep(2.25)


    print("Rotate\n")
    arduinoWrite("Rotate")
    time.sleep(1.5)


arduino.close()

# endregion