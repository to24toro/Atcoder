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

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
s = [-1]*n
q = deque([(0,0)])
while q:
    x,c = q.popleft()
    s[x] = c
    for y in g[x]:
        if s[y]<0:
            s[y] = 1-c
            q.append((y,1-c))
S = sum(s)
even = []
odd = []
for i in range(n):
    if s[i]:
        odd.append(i+1)
    else:
        even.append(i+1)
if len(odd)>=n//2:
    print(*odd[:n//2])
else:
    print(*even[:n//2])
