from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n = int(input())
L = []
K = []
for _ in range(n):
    a,b = map(int,input().split())
    if a-b<0:
        L.append((a-b,a,b))
    else:
        K.append((a-b,a,b))
INF = float('inf')
ans = -INF
res = 0
L.sort(key = lambda x:[x[1]])
K.sort(key = lambda x:[-x[2]])
for c,a,b in L:
    res += a
    ans = max(ans,res)
    res -= b
    ans = max(ans,res)
for c,a,b in K:
    res += a
    ans = max(ans,res)
    res -= b
    ans = max(ans,res)
print(ans)