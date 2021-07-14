from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

MOD = 10**9+7

n,m = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

Sum = [[0]*(m+1) for _ in range(n+1)]
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if S[i-1]==T[j-1]:
            dp[i][j] = Sum[i-1][j-1]+1
        else:
            dp[i][j] = 0
        dp[i][j] %= MOD
        Sum[i][j] = Sum[i][j-1] + Sum[i-1][j] -Sum[i-1][j-1] + dp[i][j]
        Sum[i][j] %= MOD
# print(Sum,dp)
ans = 0
for i in range(n+1):
    for j in range(m+1):
        ans += dp[i][j]
        ans %= MOD
print(ans)


