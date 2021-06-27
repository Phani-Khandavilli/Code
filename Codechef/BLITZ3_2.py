'''
June 27, Starters
'''
import math as m

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    blackMoves=m.floor(n/2)
    whiteMoves=m.floor((n+1)/2)
    blacktime=180+2*blackMoves
    whitetime=180+2*whiteMoves
    totalTime=blacktime+whitetime
    # if (n % 2 != 0):
    #     totalTime = 2 * (180 + int((n) / 2)) + 2
    # else:
    #     totalTime = 2 * (180 + int(n / 2))
    print(totalTime - (a + b))
