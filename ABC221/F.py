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

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int,input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)
res = [-1]*n

def dfs(i,d):
    for j in g[i]:
        if res[j]<0:
            res[j] = d+1
            dfs(j,d+1)
res[0] = 0
dfs(0,0)
idx = res.index(max(res))
res = [-1]*n
res[idx]=0
dfs(idx,0)
p = max(res)
idx = res.index(p//2)
res = [-1]*n
res[idx]=0
MOD = 998244353
s =[0]*n
def dfs(i,d):
    f =True
    for j in g[i]:
        if res[j]==-1:
            f =False
            res[j] = d+1
            dfs(j,d+1)
    if f:s[i]=1

dfs(idx,0)
if p%2:
    x,y = 0,0
    for i in range(n):
        if res[i]==p//2 and s[i]==1:
            x +=1
        if res[i]==p//2+1 and s[i]==1:
            y += 1

    print(x*y%MOD)
else:
    x = 0
    for i in range(n):
        if res[i]==p//2 and s[i]==1:
            x += 1
    print(pow(2,x,MOD)-1-x)