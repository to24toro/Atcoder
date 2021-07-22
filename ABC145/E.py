from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,t = map(int,input().split())
dp = [[0]*(t+1) for _ in range(n+1)]
L = [list(map(int,input().split())) for _ in range(n)]
L.sort(key = lambda x:x[0])
ans = 0
for i in range(1,n+1):
    a,b = L[i-1]
    for j in range(t):
        dp[i][j] = dp[i-1][j]
        ans = max(ans,dp[i][j]+b)
        if j-a>=0:
            dp[i][j] = max(dp[i][j],dp[i-1][j-a]+b)

print(ans)