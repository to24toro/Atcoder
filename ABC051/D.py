from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m = map(int,input().split())
g = [[] for _ in range(n)]
dic = {}
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))
    dic[(a,b)]=False
    dic[(b,a)]=False
def dijkstra(start,graph,n):
    import heapq

    dist = [float('inf')]*n

    hq = []

    heapq.heappush(hq,(0,start,-1))
    dist[start]=0
    while hq:
        d,x,z = heapq.heappop(hq)
        if dist[x]<d:
            continue
        if dist[x]>=d:
            dist[x] = d
            dic[(x,z)]=True
            dic[(z,x)]=True
        for y,d2 in graph[x]:
            if dist[y]>d+d2:
                heapq.heappush(hq,(d+d2,y,x))
    return dist
ans = 0
for i in range(n):
    d = dijkstra(i,g,n)
    # print(d)
# print(dic)
for k,v in dic.items():
    if v==False:
        ans +=1
print(ans//2)
