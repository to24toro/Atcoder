from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n = int(input())
g = [[] for _ in range(n)]
L = []
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
    L.append((a,b))
d = [-1]*n
idx = 
def dfs(i,c):
    for j in g[i]:
        if i!=j and d[j] == -1:
            d[j] = c+1
            dfs(j,c+1)
d[0] = 0
dfs(0,0)
mx = max(d)
idx = d.index(mx)
d = [-1]*n
d[idx] = 0
dfs(idx,0)
P = [0]*n
q = int(input())
for _ in range(q):
    t,e,x = map(int,input().split())
    if t == 1:
        a,b = L[e-1]
    else:
        b,a = L[e-1]
    if d[a]<d[b]:
        P[a]+=x
    else:
        P[idx]+=x
        P[b]-=x

print(d,P)
q = deque([(idx,P[idx])])
s = [0]*n
s[idx] = 1
while q:
    x,c = q.popleft()
    for y in g[x]:
        if s[y]==0:
            s[y] =1
            P[y]+=c
            q.append((y,P[y]))

for p in P:
    print(p)
