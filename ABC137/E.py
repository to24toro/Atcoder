from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,m,p = map(int,input().split())
gg = []
rg = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    gg.append((a,b,p-c))
    rg[b].append(a)

chk = [0]*n
q =deque([n-1])
chk[n-1]=1

while q:
    x = q.popleft()
    for y in rg[x]:
        if chk[y]==0:
            chk[y]=1
            q.append(y)
g = []
for a,b,c in gg:
    if chk[a]==1 and chk[b]==1:
        g.append((a,b,c))

def Bellman_ford(s,n,g):
    dist = [float('inf')]*n
    dist[s] = 0
    for i in range(n):
        update = False
        for x,y,z in g:
            if dist[y]>dist[x]+z:
                dist[y] = dist[x]+z
                update = True
        if not update:
            break
        if i ==n-1:
            return -1
    return dist
dist = Bellman_ford(0,n,g)
if dist==-1:
    print(-1)
else:
    print(max(0,-dist[-1]))
