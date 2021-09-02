from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
A = list(map(int,input().split()))
AA = []
for i,a in enumerate(A):
    AA.append((a,i))
AA.sort()
B = []
BB = list(map(int,input().split()))
for a,i in AA:
    B.append(BB[i])
dp = [[0]*(max(A)+1) for _ in range(n+1)]
mod = 998244353
dp[0][0]=1
for i in range(1,n+1):
    b = B[i-1]
    for j in range(max(A)+1):
        dp[i][j] += dp[i-1][j]
        dp[i][j]%=mod
        if j+b<=max(A):
            # print(j,b)
            dp[i][j+b] +=dp[i-1][j]
            dp[i][j+b]%=mod
        
ans = 0
mx = -1000000
# print(dp)
for i in range(n):
    a = AA[i][0]
    p = a-B[i]
    if p>=0:
        ans +=sum(dp[i][:p+1])
        ans %=mod
print(ans)
