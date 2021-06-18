from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m = map(int,input().split())
g = [[] for _ in range(n)]
ans = 0
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
for i in range(n):
    s = [0]*n
    q = deque([i])
    s[i]=1
    while q:
        x = q.popleft()
        for y in g[x]:
            if s[y]==0:
                s[y]=1
                q.append(y)
    ans += sum(s)
print(ans)

##7min