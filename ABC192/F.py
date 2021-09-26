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
n,x = map(int,input().split())
A = list(map(int,input().split()))
ans = x
s = sum(A)
for k in range(n,0,-1):
    if (x-s)//k>ans:continue
    dp = [[[-INF] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        a = A[i]
        for j in range(k+1):
            for m in range(k):
                if dp[i][j][m]==-INF:
                    continue
                dp[i+1][j][m] = max(dp[i+1][j][m],dp[i][j][m])
                t = (dp[i][j][m]+a)%k
                dp[i+1][j+1][t] = max(dp[i+1][j+1][t],dp[i][j][m]+a)
    if dp[n][k][x%k]<0:continue
    ans = min(ans,(x-dp[n][k][x%k])//k)
print(ans)