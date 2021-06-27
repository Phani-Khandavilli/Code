'''
June 27, Starters
'''

t = int(input())

def fun(a, b, c, d):
    if (a + c == 180):
        return True
    elif (b + d == 180):
        return True
    else:
        return False

for _ in range(t):
    a, b, c, d = map(int, input().split())
    if (fun(a, b, c, d)):
        print("yes")
    else:
        print("no")
