'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def ispower(num):
    lis=list(str(num))
    lis=list(map(int,lis))
    for i in lis:
        if(i%2==1):
            return False
    return True

def getgreaternum(num):
    # if(ispower(num)):
    #     return num
    # else:
    #     return getgreaternum(num+1)
    lis=list(str(num))
    lis=list(map(int,lis))
    s=''
    incremented=False
    for i in range(len(lis)):
        print('inside',s,lis[i])
        if(not incremented):
            if(lis[i]%2==1):
                s=s+str(lis[i]+1)
                incremented=True
            else:
                s=s+str(lis[i])
        else:
            s=s+'0'
    return(int(s))
            

def getlessernum(num):
    # if(ispower(num)):
    #     return num
    # else:
    #     return getlessernum(num-1)
    decremented=False
    lis=list(str(num))
    lis=list(map(int,lis))
    s=''
    for i in range(len(lis)):
        print('outside',s,lis[i])
        if(not decremented):
            if(lis[i]%2==1):
                decremented=True
                s=s+str(lis[i]-1)
            else:
                s=s+str(lis[i])
        else:
            s=s+'8'
    return int(s)

def gcd(a,b):
    if(a==0):
        return b
    else:
        return(gcd(b%a,a))

t=int(input())
for _ in range(t):
    num=int(input())
    if(ispower(num)):
        print('Unlimited Power')
    else:
        greaternum=getgreaternum(num)
        lessernum=getlessernum(num)
        print(greaternum,lessernum)
        numerator=greaternum-num
        denominator=num-lessernum
        gcdnum=gcd(denominator,numerator)
        print(str(int(numerator/gcdnum))+'/'+str(int(denominator/gcdnum)))