'''
June 27, Starters
'''

t = int(input())

def reCalculateSleepRequired(sleepRequired, units):
    if (units == 0):
        return sleepRequired
    if (units < sleepRequired):
        newSleepRequired = 2 * (sleepRequired - units)
        if(newSleepRequired < sleepRequired):
            return newSleepRequired
        else:
            return sleepRequired
    elif (units >= sleepRequired):
        return 0

for _ in range(t):
    l, sleepRequired = map(int, input().split())
    s = input()
    unitCount = 0
    for i in range(l):
        if (s[i] == '0'):
            unitCount += 1
            if (i == l - 1):
                sleepRequired = reCalculateSleepRequired(sleepRequired, unitCount)
        else:
            sleepRequired = reCalculateSleepRequired(sleepRequired, unitCount)
            unitCount = 0
        if(sleepRequired <= 0):
            break

    if (sleepRequired != 0):
        print('NO')
    else:
        print('YES')
