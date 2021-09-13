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
dp = [[INF]*(n+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
    h = H[i]
    for j in range(1,n+1):
        for k in range(i):
            dp[i][j] = min(dp[i][j],dp[k][j-1]+max(0,h-H[k]))
ans = INF
# print(dp)
for i in range(n+1):
    ans = min(ans,dp[i][n-cnt])
print(ans)