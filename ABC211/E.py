from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n = int(input())
k = int(input())
S = [input() for _ in range(n)]

ans = 0

set_ = set()


for i in range(n):
    for j in range(n):
        if S[i][j] =='.':
            set_.add(1<<(i*n+j))

for kk in range(k):
    nxt = set()
    for s in set_:
        for i in range(n):
            for j in range(n):
                if S[i][j]=='.' and not(s & (1<<(i*n+j))):
                    ok = False
                    for di,dj in [(1,0),(0,1),(0,-1),(-1,0)]:
                        I = i+ di
                        J = j+ dj
                        if 0<=I<n and 0<=J<n:
                            if S[I][J]=='.' and (s & (1<<(I*n+J))):
                                ok = True
                    if ok:
                        nxt.add(s|(1<<(i*n+j)))
    # print(len(set_),len(nxt))
    if kk!=k-1:
        set_ = nxt
print(len(set_))

