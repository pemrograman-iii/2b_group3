import serial

def tryARD():
    set = serial.Serial("AHOY", 9600)
    print(set.name)

tryARD()