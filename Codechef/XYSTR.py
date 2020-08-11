t=int(input())
for _ in range(t):
	string=input()
	numPairs=0
	length=len(string)
	i=0
	while(i<length-1):
		# print(i,length)
		if(string[i]=='x'and string[i+1]=='y'):
			numPairs+=1
			i+=2
		elif(string[i]=='y' and string[i+1]=='x'):
			numPairs+=1
			i+=2
		else:
			i+=1
	print(numPairs)