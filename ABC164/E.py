from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,m,s = map(int,input().split())
s = min(s,2500)

g = [[] for _ in range(n)]
for _ in range(m):
    u,v,a,b = map(int,input().split())
    u-=1
    v-=1
    g[u].append((v,a,b))
    g[v].append((u,a,b))
#通貨の交換を自己ループにする
for i in range(n):
    c,d = map(int,input().split())
    g[i].append((i,-c,d))
inf = float('inf')
dp = [[inf]*2501 for _ in range(n)]
dp[0][s] = 0
hq = [(0, s, 0)]
heapify(hq)
while hq:
    t,c,v = heappop(hq)
    if dp[v][c]<t:
        continue
    for u,a,b in g[v]:
        if c<a:
            continue
        ng = c-a
        if ng>2500:
            ng = 2500
        f = 0
        for i in range(ng,-1,-1):
            if dp[u][i]>t+b:
                dp[u][i]=t+b
                f = 1
            else:
                break
        if f:
            heappush(hq,(t+b,ng,u))
for i in range(1,n):
    print(min(dp[i]))