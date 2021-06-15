from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m,s,t = map(int,input().split())
s-=1
t-=1
ge = [[] for _ in range(n)]
gs = [[] for _ in range(n)]

for _ in range(m):
    u,v,a,b = map(int,input().split())
    u-=1
    v-=1
    ge[u].append((v,a))
    ge[v].append((u,a))
    gs[u].append((v,b))
    gs[v].append((u,b))


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

de = dijkstra(s,ge,n)
ds = dijkstra(t,gs,n)

ans = []
for i in range(n-1,-1,-1):
    if i==n-1:
        ans.append(de[i]+ds[i])
    else:
        ans.append(min(ans[-1],de[i]+ds[i]))
for a in ans[::-1]:
    print(10**15-a)

