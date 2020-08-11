t=int(input())
for _ in range(t):
	numPpl=int(input())
	queue=list(map(int,input().split()))
	dic={5:0,10:0,15:0}
	ans=True
	for index in range(numPpl):
		amount=queue[index]
		change=amount-5
		# if(change==0):
		# 	dic[5]=dic[5]+1
		# elif(change==5):
		# 	if(dic[5]>0):
		# 		dic[5]=dic[5]-1
		# 		dic[10]=dic[10]+1
		# 	else:
		# 		ans=False
		# 		break
		# elif(change==10):
		# 	if(dic[10]>0):
		# 		dic[10]=dic[10]-1
		# 		dic[15]=dic[15]+1
		# 	else:
		# 		ans=False
		# 		break
		if(change==0):
			dic[amount]=dic[amount]+1
		else:
			if(dic[change]>0):
				dic[change]=dic[change]-1
				dic[amount]=dic[amount]+1
			else:
				ans=False
				break
	if(ans):
		print('YES')
	else:
		print('NO')

