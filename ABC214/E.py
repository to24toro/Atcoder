from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    d = defaultdict(list)
    for _ in range(n):
        l,r = map(int,input().split())
        d[l].append(r)
    q = []
    e = sorted(d.items(),reverse=True)
    i = 0
    f =True
    while e:
        k,v = e.pop()
        i = max(i,k)
        for r in v:
            heappush(q,r)
        while q:
            r = heappop(q)
            if i>r:
                f = False
                break
            i += 1
            if i in d:
                break
    if f:
        print('Yes')
    else:
        print('No')
