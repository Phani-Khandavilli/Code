n=int(input())
for _ in range(n):
	order=input()
	lis=order.split('0')
	groupcount=0
	for i in lis:
		if(i!=''):
			groupcount+=1
	print(groupcount)