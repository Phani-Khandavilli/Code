t=int(input())

for _ in range(t):
	a,b,x=map(int,input().split())
	n=((b-a)//x)
	print(n)
