import csv
with open("abc.csv",'r')as efile:
	data=csv.reader(efile)
	for i in data:
		print(i)
