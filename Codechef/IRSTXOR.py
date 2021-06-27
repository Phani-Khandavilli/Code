import math as m

t=int(input())
for _ in range(t):
	c=int(input())
	d=m.ceil(m.log(c,2))
	maxval=2**d
	maxprod=1
	for a in range(int(maxval/2)):
		b=c^a
		if(b<maxval):
			prod=a*b
			if(prod>maxprod):
				maxprod=prod
	print(maxprod)
