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
in_cnt = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    in_cnt[b] += 1
left = [True]*n
def topological_sort(n,g,in_cnt):
    res = []
    from collections import deque
    queue = deque([i for i in range(n) if in_cnt[i]==0])
    while len(queue)!=0:
        u = queue.popleft()
        res.append(u)
        for v in g[u]:
            in_cnt[v]-=1
            if in_cnt[v]==0:
                queue.append(v)
    return res
print(topological_sort(n,g,in_cnt))
for s in range(n):
    q = deque([(s,{s})])
    f =False
    seen = [-1]*n
    seen[s] = 0
    while q:
        x,path = q.popleft()
        for y in g[x]:
            if seen[y]==0:
                f =True
                break
            elif seen[y] ==-1:
                seen[y] = seen[x] + 1
                nx = path.copy()
                nx.add(y)
                q.append((y,nx))
            else:
                if y in path:
                    break
        if f:
            print(len(path))
            for p in path:
                print(p+1)
            exit()
print(-1)

  