import csv

file = open('1.csv', 'r')
reader = csv.reader(file)
for data in reader:
	print(data)