'''
June 27, Starters
wrong answer
error code: tle

Reason: might most probably not work with python as it uses more time in general
Similar brute force logic worked with c and c++

Correct approach: Must use fenwick tree
https://en.wikipedia.org/wiki/Fenwick_tree
'''

def fun(array, l, r, x):
    for i in range(l, r + 1):
        array[i] = array[i] + (x + i - l) ** 2

n, numqueries = map(int, input().split())
array = list(map(int, input().split()))
for queryNumber in range(numqueries):
    query = list(map(int, input().split()))
    if (query[0] == 2):
        print(array[query[1] - 1])
    else:
        fun(array, query[1]-1, query[2]-1, query[3])
