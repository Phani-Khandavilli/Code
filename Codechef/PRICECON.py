t=int(input())
for _ in range(t):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	loss=0
	for i in arr:
		if(i>k):
			loss=loss+(i-k)
	print(loss)