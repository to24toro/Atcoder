from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

def dijkstra(start,graph,n):
    import heapq

    dist = [float('inf')]*n

    hq = []

    heapq.heappush(hq,(0,start))
    dist[start]=0
    while hq:
        d,x = heapq.heappop(hq)
        if dist[x]<d:
            continue
        for y,d2 in graph[x]:
            if dist[y]>d+d2:
                dist[y]=d+d2
                heapq.heappush(hq,(d+d2,y))
    return dist

n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))
dx = dijkstra(0,g,n)
dy = dijkstra(n-1,g,n)
# print(dx,dy)
for i in range(n):
    print(dx[i]+dy[i])