import math as m

# t=int(input())
# for _ in range(t):
# 	D,d,P,Q=map(int,input().split())
# 	numTimesIncremented=m.floor(D/d)
# 	numdaysLeft=D%d
# 	value=d*(numTimesIncremented/2)*(2*P+(numTimesIncremented-1)*Q) + (numdaysLeft * (P + (numTimesIncremented * Q)))
# 	# if(numdaysLeft!=0):
# 	# 	value = value + (numdaysLeft * (P + (numTimesIncremented * Q)))
# 	print(int(value))


T = int(input())
for i in range(T):
    D, d, P, Q = map(int, input().split())
    n = D//d
    ans = n*P*d + (Q*(n*(n-1))//2)*d +(D%d)*(P+n*Q)
    print(ans)
