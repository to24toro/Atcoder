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

def dfs(i,pre,rest):
    res = rest
    used = 1
    if i>0:used+=1
    if k<len(g[i]):return 0
    for j in g[i]:
        if j==pre:continue
        res*=dfs(j,i,k-used)
        res%=mod
        used+=1
    return res%mod

res = (dfs(0,-1,k))
print(res)