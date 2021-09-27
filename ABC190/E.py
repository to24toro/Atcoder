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

n,m = map(int,input().split())
d = defaultdict(lambda :defaultdict(int))
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    d[a][b] = 1
    d[b][a] = 1
    g[a].append(b)
    g[b].append(a)
k = int(input())
C = list(map(lambda x:int(x)-1, input().split()))
dp = [[-1]*n for _ in range(1<<n)]

def rec(s,v):
    if dp[s][v]>=0:
        return dp[s][v]
    if (s==(1<<n)-1 and v==0):
        dp[s][v]=0
        return dp[s][v]
    res = float('inf')
    for u in range(n):
        if not ((s>>u)&1):
            if d[v][u]:
                res = min(res,rec(s|1<<u,u)+d[v][u])
    dp[s][v]=res
    return res

rec(0,0)
def bfs(s):
    cost = [INF] * n
    cost[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for y in g[x]:
            if cost[y] == INF:
                cost[y] = cost[x] + 1
                q.append(y)
    return [cost[c] for c in C]
cost = [bfs(c) for c in C]
