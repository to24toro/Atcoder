from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import numpy as np
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)

def dfs(i):
    s = [-1]*n
    q = deque([(i,0)])
    s[i] = 0
    while q:
        x,cnt = q.popleft()
        for y in g[x]:
            if s[y]<0:
                s[y] = cnt + 1
                q.append((y,cnt+1))
    return max(s), s.index(max(s))

_,i = dfs(0)
ans,_ = dfs(i)
print(ans+1)
