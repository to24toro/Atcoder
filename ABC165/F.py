from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
A = list(map(int,input().split()))
g = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(lambda x:int(x)-1,input().split())
    g[u].append(v)
    g[v].append(u)
ans = [-1]*n
LIS = [INF]*n
def dfs(u,p):
    global ans
    index = bisect_left(LIS,A[u])
    bf = LIS[index]
    LIS[index] = A[u]
    ans[u] = bisect_left(LIS,INF)
    for v in g[u]:
        if v!=p:
            dfs(v,u)
    LIS[index] = bf
    return
dfs(0,-1)
print(*ans,sep='\n')