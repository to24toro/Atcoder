from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

mod = 10**9+7

n,k = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
def dfs(now,pre,val):
    res = val
    c = 1
    if now!=0:c+=1
    for nxt in g[now]:
        if nxt!=pre:
            res *= dfs(nxt,now,k-c)
            c+=1
            res%=mod
    return res

print(dfs(0,-1,k))