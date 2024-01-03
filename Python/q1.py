a=[]
n=int(input("enter length :"))
for i in range(n):
	b=int(input("enter the elements to the list :"))
	a.append(b)
print(a)
sum=0
for i in range(n):
	sum=sum+a[i]
print("sum of elements in the list :",sum)		
