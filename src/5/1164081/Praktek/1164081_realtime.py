import serial
import csv

def rSerial():
	ser = serial.Serial('COM3', 9600, timeout=2)
	x = ser.readline()
	return x

def wCSV():
    ser = serial.Serial('COM3',9600)
    with open('1164081_try.csv', mode='w') as csv_file:
        fieldnames = ['coba']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        while (1):
            data = ser.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'coba': data})      
wCSV()