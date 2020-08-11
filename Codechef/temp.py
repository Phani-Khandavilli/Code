lis=[1,2,3]
def check(num):
	if(num in lis):
		return True
	else:
		return False
def add(num):
	lis.append(num)
n=int(input("enter number"))
print(check(n))
ans=input("do u want to add")
if(ans=='y'):
	add(n)
print(lis)