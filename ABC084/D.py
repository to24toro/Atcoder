Q=  int(input())
dp = [False]*(100001)
for i in range(2,100001):
    if not dp[i]:
        for j in range(2*i,100001,i):
            dp[j] = True
A = []
for i in range(3,100001):
    if not dp[i] and not dp[(i+1)//2]:
        A.append(i)
from bisect import bisect_left, bisect_right
queries = []
for _ in range(Q):
    l,r = map(int,input().split())
    queries.append([l,r])
for l,r in queries:
    idl = bisect_left(A,l)
    idr = bisect_right(A,r)
    print(idr-idl)