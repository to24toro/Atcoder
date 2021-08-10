from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]
def scc(n,g,rg):
    order = []
    used = [0]*n
    group = [None]*n
    def dfs(s):
        used[s] = 1
        for t in g[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s,col):
        group[s] = col
        used[s] = 1
        for t in rg[s]:
            if not used[t]:
                rdfs(t,col)
    for i in range(n):
        if not used[i]:
            dfs(i)
    used = [0]*n
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s,label)
            label += 1
    return label, group
n,m = map(int,input().split())
g = [[] for _ in range(n)]
rg = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    rg[b].append(a)
label, group = scc(n,g,rg)
dic = defaultdict(int)
for g in group:
    dic[g] += 1
ans = 0
for l in range(label):
    cnt = dic[l]
    ans += cnt*(cnt-1)//2
print(ans)
