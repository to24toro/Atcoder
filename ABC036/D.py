from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
MOD = 10**9+7
n = int(input())
g = [[] for _ in range(n)]
w = [0]*n
b = [0]*n
for _ in range(n-1):
    aa,bb = map(int,input().split())
    aa-=1
    bb-=1
    g[aa].append(bb)
    g[bb].append(aa)

ans = 0
def dfs(s,pre):
    ww = 1
    bb = 1
    for t in g[s]:
        if pre == t:continue
        tw,tb = dfs(t,s)
        ww*=(tw+tb)
        bb*=tw
        ww%=MOD
        bb%=MOD
    w[s]=ww
    b[s]=bb
    return w[s],b[s]
dfs(0,-1)
print((w[0]+b[0])%MOD)

