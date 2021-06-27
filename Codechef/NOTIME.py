n,h,x=map(int,input().split())
timezones=list(map(int,input().split()))
requiredTime=h-x
if(requiredTime>0):
	if(requiredTime in timezones):
		print("YES")
	else:
		print("NO")
else:
	print("YES")