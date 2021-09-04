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
    u,v = map(int,input().split())
    u-=1
    v-=1
    g[u].append(v)
s,t = map(int,input().split())
s-=1
t-=1
d = [[INF,INF,INF] for _ in range(n)]
d[s][0] = 0
q = deque([(s,0,0)])
while q:
    x,c,cost = q.popleft()
    for y in g[x]:
        if d[y][(c+1)%3]==INF:
            d[y][(c+1)%3] = cost+1
            q.append((y,(c+1)%3,cost+1))
print(d[t][0]//3 if d[t][0]!=INF else -1)

