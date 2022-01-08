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

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1;b-=1
    g[a].append(b)
    g[b].append(a)

def bfs(s,g,n):
    INF = float('inf')
    dist = [INF]*n
    dist[s] = 0
    q = deque([(s,0)])
    while q:
        s,c = q.popleft()
        for t in g[s]:
            if t!=s and dist[t]>c+1:
                dist[t] = c+1
                q.append((t,c+1))
    return dist

A = bfs(0,g,n)
B = bfs(n-1,g,n)
fennec = 0
sunuke = 0
for i, (a,b) in enumerate(zip(A,B)):
    if a<=b:
        fennec +=1
    else:
        sunuke += 1
if fennec>sunuke:
    print('Fennec')
else:
    print('Snuke')
    