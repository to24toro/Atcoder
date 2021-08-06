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
X = []
for _ in range(m):
    l,r,c = map(int,input().split())
    l-=1
    r-=1
    X.append((l,r,c))
X.sort()
g = [[] for _ in range(n)]
prev = -1
for l,r,c in X:
    g[l].append((c,r))
    if prev>l:
        l = prev
        if prev>r:
            continue
    prev = r
    for i in range(r,l,-1):
        g[i].append((0,i-1))

# print(g)
dist = [INF]*n
hq = []
heappush(hq,(0,0))
dist[0] = 0
while hq:
    c,s = heappop(hq)
    if dist[s]<c:
        continue
    for dc,t in g[s]:
        if dist[t] > c + dc:
            dist[t] = c + dc
            heappush(hq,(c+dc,t))
print(dist[-1] if dist[-1]!=INF else -1)

