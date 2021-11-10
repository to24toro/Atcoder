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
def topological_sort(n,g,in_cnt):
    res = []
    queue = ([i for i in range(n) if in_cnt[i]==0])
    heapify(queue)
    while len(queue)!=0:
        u = heappop(queue)
        res.append(u)
        for v in g[u]:
            in_cnt[v]-=1
            if in_cnt[v]==0:
                heappush(queue,v)
    return res

n,m = map(int,input().split())
g = [[] for _ in range(n)]
in_cnt = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    a-=1;b-=1
    g[a].append(b)
    in_cnt[b]+=1
res = topological_sort(n,g,in_cnt)
if len(res)!=n:
    print(-1)
else:
    ans = []
    for r in res:
        ans.append(r+1)
    print(*ans)