
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

q = deque([(0,-1)])
s = [0]*n
s[0] = 1
dic = defaultdict(int)
ans = -INF
while q:
    x,c = q.popleft()
    p = 0
    for y in g[x]:
        if not s[y]:
            s[y] = 1
            if p==c:
                p += 1
            dic[(x,y)] = p
            dic[(y,x)] = p
            ans = max(ans,p)
            q.append((y,p))
            p += 1
print(ans+1)
for a,b in L:
    print(dic[(a,b)]+1)
            

