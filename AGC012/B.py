from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m = map(int,input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)

q = int(input())
Q = [tuple(map(int,input().split())) for _ in range(q)]
heights = [-1]*n
colors = [0]*n

for u,d,c in Q:
    u-=1
    if d<=heights[u]:
        continue
    heights[u]=d
    stack = [(u,d)]
    while stack:
        v,h = stack.pop()
        if colors[v]==0:
            colors[v]=c
        if h>0:
            for nv in g[v]:
                if h-1>heights[nv]:
                    heights[nv]=h-1
                    stack.append((nv,h-1))
print(*colors,sep = '\n')