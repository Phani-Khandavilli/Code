t=int(input())
for _ in range(t):
	n=int(input())
	evennum=[2]
	oddnum=[1]
	for row in range(n):
		if(row%2==0):
			# firstnum=evennum
			# secondnum=oddnum
			number=[oddnum,evennum]
		else:
			# firstnum=oddnum
			# secondnum=evennum			
			number=[evennum,oddnum]
		string=''
		for col in range(n):
			if(col%2==0):
				# string=string+(str(firstnum)+' ')
				string=string+(str(number[0][0])+' ')
				number[0][0]=number[0][0]+2
			else:
				string=string+(str(number[1][0])+' ')
				number[1][0]=number[1][0]+2
		print(string)