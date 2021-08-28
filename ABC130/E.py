from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,m = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1
for j in range(m+1):
    dp[0][j] = 1
mod = 10**9+7
for i in range(1,n+1):
    for j in range(1,m+1):
        if S[i-1]==T[j-1]:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod
        else:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]) % mod
print(dp[n][m]%mod)