from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
mod = 998244353
n,m,k = map(int,input().split())
dp = [[0]*n for _ in range(k+1)]
g = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)

dp[0][0] = 1
for i in range(1,k+1):
    s =sum(dp[i-1])
    for j in range(n):
        tmp = 0
        for jj in g[j]:
            tmp += dp[i-1][jj]
            tmp %= mod
        dp[i][j] += s-tmp-dp[i-1][j]
        dp[i][j] %= mod
# print(dp)
print(dp[-1][0]%mod)