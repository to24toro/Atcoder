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
n,u,v = map(int,input().split())
u-=1
v-=1
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
def bfs(x):
    s = [INF]*n
    s[x] = 0
    q = deque([(x,0)])
    while q:
        x,c = q.popleft()
        for y in g[x]:
            if s[y]>c+1:
                s[y] = c+1
                q.append((y,c+1))
    return s
taka = bfs(u)
aoki = bfs(v)
ans = -INF
for i in range(n):
    if aoki[i]>taka[i]:
        ans = max(ans,aoki[i]-1)
print(ans)