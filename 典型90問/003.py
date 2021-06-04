from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
res = [-1]*n

def dfs(i,d):
    for j in g[i]:
        if res[j]<0:
            res[j] = d+1
            dfs(j,d+1)
res[0]=0
dfs(0,0)
idx = res.index(max(res))
res = [-1]*n
res[idx]=0
dfs(idx,0)
print(max(res)+1)