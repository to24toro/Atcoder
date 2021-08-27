from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,k = map(int,input().split())
V = list(map(int,input().split()))
hq = []
ans = -INF
for l in range(k+1):
    for r in range(k+1):
        if l+r>k:
            continue
        if l+r>n:
            continue
        m = max(k-l-r,0)
        L = V[:l]
        R = V[n-r:]
        LR = L+R
        heapify(LR)
        cur = sum(LR)
        ans = max(ans,cur)
        for _ in range(m):
            if LR:
                cur-=heappop(LR)
                ans = max(cur,ans)
print(ans)