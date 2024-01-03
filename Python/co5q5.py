import pandas
import csv
field=['rollno','name','age']
sdict=[{'rollno':10,'name':'alfahm','age':21},
       {'rollno':11,'name':'dragonfruit','age':24},
       {'rollno':12,'name':'Shawarma','age':26}]
with open("dpt.csv",'w')as dfile:
	writer=csv.DictWriter(dfile,fieldnames=field)
	writer.writeheader
	writer.writerows(sdict)    
data=pandas.read_csv("dpt.csv")	   
print(data)
