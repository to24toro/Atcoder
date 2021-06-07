from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,q = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
cnt = [0]*n
for _ in range(q):
    p,x = map(int,input().split())
    p-=1
    cnt[p]+=x
q = deque([(0,cnt[0])])
seen = [0]*n
seen[0]=1
while q:
    u,c = q.popleft()
    for v in g[u]:
        if not seen[v]:
            seen[v]=1
            cnt[v]+=c
            q.append((v,cnt[v]))
print(*cnt)
