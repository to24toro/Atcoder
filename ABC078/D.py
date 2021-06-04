N,Z,W = map(int,input().split())
A = list(map(int,input().split()))

if N==1:
    print(abs(W-A[0]))
else:
    print(max(abs(W-A[-1]),abs(A[-2]-A[-1])))

import sys

sys.setrecursionlimit(1<<20)
memo = [[-1,-1] for _ in range(N)]

def f(id,turn,x,y):
    if id==N:
        return abs(x-y)
    if memo[id][turn]>=0:return memo[id][turn]
    if turn==0:
        ma = -1
        for i in range(N):
            ma = max(ma,f(i+1,1-turn,A[i],y))
        memo[id][turn]=ma
        return ma
    else:
        mi = float('inf')
        for i in range(N):
            mi = min(mi,f(i+1,1-turn,x,A[i]))
        memo[id][turn]=mi
        return mi
print(f(0,0,Z,W))