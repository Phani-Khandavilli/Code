t=int(input())
for _ in range(t):
	k1,k2,k3,v=map(float,input().split())
	speed=k1*k2*k3*v
	time=100/speed
	roundTime=round(time,2)
	if(roundTime<9.58):
		print("YES")
	else:
		print("NO")