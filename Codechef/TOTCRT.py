'''
June 27, Starters
'''
t = int(input())

for _ in range(t):
    n = int(input())
    queDict = {}
    for i in range(3*n):
        que, count = input().split()
        count = int(count)
        if (queDict.get(que) == None):
            queDict[que] = count
        else:
            queDict[que] = queDict[que] + count
    listValues=[]
    for i in queDict.values():
        listValues.append(i)
    ans=""
    listValues.sort()
    for i in listValues:
        ans=ans+str(i)+" "
    print(ans.strip())
