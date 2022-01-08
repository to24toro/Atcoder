from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,k = map(int,input().split())
ans = 0
L = [list(map(int,input().split())) for _ in range(n)]
for i in range(31,-1,-1):
    if (k>>i)&1:
        v = 0
        for a,b in L:
            if not (a>>i)&1:
                v += b
        ans = max(ans,v)
    else:
        tmp = []
        for a,b in L:
            if not(a>>i)&1:
                tmp.append([a,b])
        L = tmp
ans = max(ans,sum(b for a,b in L))
print(ans)

