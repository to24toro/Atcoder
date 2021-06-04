from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
mod = 10**9+7

n = int(input())
D = [int(input()) for _ in range(n)]
D.sort()
L = []
R = []
for i in range(n):
    d = D[i]//2
    e = D[i]*2
    idx = bisect_right(D,d)
    L.append(idx)
    idy = bisect_left(D,e)
    R.append(n-idy)
# print(R)
R = R[::-1]
RR = list(accumulate(R))
RR = RR[::-1]
# print(RR)
ans = 0
for i in range(n):
    l = L[i]
    idx = bisect_left(D,D[i]*2)
    if idx ==n:
        continue
    else:
        ans += l*RR[idx]
    ans %=mod
print(ans)