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
d = [[INF]*n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
L = []
g = [[] for _ in range(n)]
for i in range(m):
    s,t = map(int,input().split())
    s-=1
    t-=1
    g[s].append(t)
    L.append((s,t))
# print(d)
for s,t in L:
    # if a<d[0][s]+d[t][n-1]+d[s][t]:
    #     print(a)
    # else:
    #     hq = [(0,0)]
    #     heapify(hq)
    #     dist = [INF]*n
    #     while hq:
    #         x,c = heappop(hq)
    #         if dist[x]<c:
    #             continue
    #         for y in g[x]:
    #             if x==s and y ==t:
    #                 continue
    #             if dist[y]>c+1:
    #                 dist[y] = c+1
    #                 heappush(hq,(y,c+1))
    #     print(dist[-1] if dist[-1]!=INF else -1)
    q = deque([(0,0)])
    ss = [INF]*n
    ss[0] = 0
    while q:
        x,c = q.popleft()
        for y in g[x]:
            if x==s and y==t:continue
            if ss[y]==INF:
                ss[y] = c
                q.append((y,c+1))
    # print(ss)         
    print(-1 if ss[-1]==INF else ss[-1])
