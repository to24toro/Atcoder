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
g = [[] for _ in range(n)]
for _ in range(m):
    x,y = map(int,input().split())
    x-=1
    y-=1
    g[x].append(y)
dp = [0]*(1<<n)
dp[0] = 1
for bit in range(1<<n):
    for i in range(n):
        if (bit>>i)&1==1:
            for j in g[i]:
                if (bit>>j)&1:
                    break
            else:
                dp[bit] += dp[bit^(1<<i)]
print(dp[(1<<n)-1])