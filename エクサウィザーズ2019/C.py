from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,q = map(int,input().split())
S = input()
W = defaultdict(list)
for i,s in enumerate(S):
    W[s].append(i)
D = defaultdict(int)
for _ in range(q):
    t,d = map(str,input().split())
    if d=='L':
        D[t] -= 1
    else:
        D[t] += 1
L,R = -INF,INF
for w,LL in W.items():
    d = D[w]
    for l in LL:
        tmp = l + d
        if tmp<0:
            L = max(L,l)
        if tmp>n-1:
            R = min(R,l)
ans = n
if L!=-INF:
    ans-=L+1
if R!=INF:
    ans-=n-R
print(ans)

