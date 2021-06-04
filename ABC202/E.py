from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())

P = list(map(lambda z:int(z)-1,input().split()))

g = [[] for _ in range(n)]
for i,p in enumerate(P):
    # g[i+1].append(p)
    g[p].append(i+1)

q = int(input())

depth = [0]*n
def dfs(v, p, d):
    for nv in g[v]:
        if nv == p: continue
        depth[nv] = d + 1
        dfs(nv, v, d + 1)
depth[0] = 1
dfs(0,0,1)
L = [[0,0] for _ in range(n)]
def dfs(i,cnt):
    L[i][0] = cnt
    for j in g[i]:
        cnt = dfs(j,cnt+1)
    cnt += 1
    L[i][1] = cnt
    return cnt
dfs(0,1)
dic = defaultdict(list)
dic2 = defaultdict(list)
for i in range(n):
    d = depth[i]
    dic[d].append(L[i][0])

    dic2[d].append(L[i][1])
for k,v in dic.items():
    dic[k].sort()
    dic2[k].sort()
for _ in range(q):
    u,d = map(int,input().split())
    u-=1
    if depth[u]-1>d:
        print(0)
    elif depth[u]-1==d:
        print(1)
    else:
        LL = dic[d+1]
        RR = dic2[d+1]
        l,r = L[u]
        ll = bisect_left(LL,l)
        rr = bisect_left(RR,r)
        print(rr-ll)
