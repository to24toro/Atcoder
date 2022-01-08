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
mod = 998244353
n,d = map(int,input().split())
A = list(map(int,input().split()))
set_ = set(A)
D = [0]*(n+1)
L = []
P = []
for i,a in enumerate(A):
    if a==-1:
        L.append([i-d,i+d])
for i in range(1,n+1):
    if i not in set_:
        P.append(i)

for p in P:
    for l,r in L:
        if l<=p<=r:
            D[p] += 1

dp = [[0]*(n+1) for _ in range(len(L))]
S = [[0]*(n+1) for _ in range(len(L))]
l0,r0 = L[0]
for i in range(max(l0,1),min(r0+1,n+1)):
    if i not in set_:
        dp[0][i] = 1
for i in range(1,n+1):
    S[0][i] = S[0][i-1]+dp[0][i]
print(dp)
print(S)
for i in range(1,len(L)):
    l,r = L[i]
    for j in range(max(l,1),min(r+1,n+1)):
        if j in set_:
            dp[i][j] = 0
        else:
            dp[i][j] += S[i-1][j]
            dp[i][j] %= mod
        S[i][j] = S[i-1][j]
        S[i][j] = S[i][j-1]+dp[i][j]
    for j in range(min(r+1,n+1),n+1):
        S[i][j] = S[i][j-1]+dp[i][j]
ans = 0
print(dp)
print(S)
for d in dp[-1]:
    ans += d
    ans %=mod
print(ans)

