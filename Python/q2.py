a=[]
n=int(input("enter length :"))
for i in range(n):
	b=int(input("enter the elements to the list :"))
	a.append(b)

l1=a[0]
for i in range(n):
	if a[i]>l1:
		l1=a[i]
print(l1," is the largest number ")
l1=a[0]
for i in range(n):
	if a[i]<l1:
		l1=a[i]
print(l1," is the smallest number ")	
a=list(set(a))
print(a)	

