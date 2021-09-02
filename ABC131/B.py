from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,l = map(int,input().split())
L = [l + i -1 for i in range(1,n+1)]
s = sum(L)
ans = INF
res = s
for l in L:
    if abs(l)<ans:
        res = s-l
        ans = abs(l)
print(res)