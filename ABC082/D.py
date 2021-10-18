from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
S = input()
x,y = map(int,input().split())
t = 0
cnt = 0
X,Y = [],[]
for s in S:
    if s=='F':
        cnt += 1
    else:
        if t == 0:
            X.append(cnt)
        else:
            Y.append(cnt)
        t = 1-t
        cnt = 0
if cnt:
    if t==0:
        X.append(cnt)
    else:
        Y.append(cnt)
if abs(x)>sum(X) or abs(y)>sum(Y):
    print('No');exit()
xx =X[0] if X else 0
X = X[1:]
def helper(L,x):
    if not L:
        if x:
            dp = [0]*(2*abs(x)+1)
            dp[x+x]=1
            return [dp]
        else:
            return [[]]
    n = len(L)
    s = sum(L)+x
    dp = [[0]*(2*s+1) for _ in range(n+1)]
    dp[0][s+x]=1
    for i in range(1,n+1):
        l = L[i-1]
        for j in range(2*s,-1,-1):
            if j+l<2*s+1:
                dp[i][j+l] = max(dp[i-1][j],dp[i][j+l])
            if j-l>=0:
                dp[i][j-l] = max(dp[i-1][j],dp[i][j-l])
    return dp

dpx = helper(X,xx)[-1]
dpy = helper(Y,0)[-1]
# print(dpx,dpy)
if not dpx and not dpy:
    if x==0 and y==0:
        print('Yes')
    else:
        print('No')
    exit()
if not dpy:
    if y!=0:
        print('No');exit()
    else:
        if dpx[x+sum(X)+xx]==1:
            print('Yes')
        else:
            print('No')
        exit()


if not dpx:
    if x!=0:
        print('No');exit()
    else:
        if dpy[y+sum(Y)]==1:
            print('Yes')
        else:
            print('No')
        exit()

px = x+sum(X)+xx
py = y + sum(Y)

if px <len(dpx) and py<len(dpy) and dpx[x+sum(X)+xx]==1 and dpy[y+sum(Y)]==1:
    print('Yes')
else:
    print('No')
