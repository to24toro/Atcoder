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
A = [(a,i+1) for i,a in enumerate(A)]
A.sort(reverse=True)
dp = [[0]*(n+1) for _ in range(n+1)]
for l in range(1,n+1):
    a,p = A[l-1]
    for i in range(l+1):
        j = l-i
        if i-1>=0:
            dp[i][j] = max(dp[i-1][j]+a*(p-i),dp[i][j])
        if j-1>=0:
            dp[i][j] = max(dp[i][j-1]+a*(n-j+1-p),dp[i][j])
ans = 0
for i in range(n+1):
    ans = max(ans,dp[i][n-i])
print(ans)

