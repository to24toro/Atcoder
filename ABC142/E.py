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
cost = []
L = []
for _ in range(m):
    a,b = map(int,input().split())
    C = list(map(lambda x:int(x)-1,input().split()))
    s = ['0']*n
    for c in C:
        s[c]='1'
    L.append(int(''.join(s),2))
    cost.append(a)
dp = [[INF]*(1<<n) for _ in range(m+1)]
dp[0][0] = 0
for i in range(m):
    c = cost[i]
    dp[i+1] = dp[i]
    for j in range(1<<n):
        dp[i+1][j|L[i]] = min(dp[i][j]+c,dp[i+1][j|L[i]])
# print(dp)
print(dp[-1][-1] if dp[-1][-1] !=INF else -1)
