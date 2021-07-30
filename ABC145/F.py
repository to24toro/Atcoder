from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
def dp(i,j,val):
    return [[val]*j for _ in range(i)]
INF = float('inf')
n,cnt = map(int,input().split())
H = [0] + list(map(int,input().split()))
dp = [dp(301,302,INF) for _ in range(301)]
dp[0][0][0] = 0
ans = INF
for i in range(n):
    for j in range(n+1):
        for k in range(cnt+1):
            if dp[i][j][k]==INF:continue
            dp[i+1][i+1][k] = min(dp[i+1][i+1][k],dp[i][j][k] + max(0,H[i+1]-H[j]))
            dp[i+1][j][k+1] = min(dp[i+1][j][k+1],dp[i][j][k])
            ans = min(ans,dp[n][j][k])
print(ans)

