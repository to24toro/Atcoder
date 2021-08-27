from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,m = map(int,input().split())
L = []
for i in range(m):
    l = list(map(int,input().split()))
    L.append(l[1:])
P = list(map(int,input().split()))
ans = 0
for bit in range(1<<n):
    set_ = set()
    res = 0
    for ii in range(n):
        if bit&(1<<ii):
            set_.add(ii+1)
    for i in range(m):
        cnt = 0
        l = L[i]
        for j in range(len(l)):
            if l[j] in set_:
                cnt += 1
        if cnt%2==P[i]:
            res += 1
    if res==m:
        ans += 1
print(ans)

