from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
T = list(map(int,input().split()))
T.sort(reverse=True)
dp = [[0]*(sum(T)+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    t = T[i-1]
    for j in range(sum(T)+1):
        dp[i][j] |=dp[i-1][j]
        if j>=t:
            dp[i][j]|=dp[i-1][j-t]
ans = -1
for i in range(sum(T)+1):
    if i<sum(T)/2:
        continue
    if dp[-1][i]:
        ans = i
        break
print(ans)

##20min