from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
from functools import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
T = int(input())
RES = []
@lru_cache
def solve(n):
    if n==0:
        return 0
    for k in range(1,6):
        for r in range(k,3*k+1):
            if (n-r)%10==0 and solve((n-r)//10)<=k:
                return k
for _ in range(T):
    n = int(input())
    RES.append(solve(n))
print(*RES,sep = '\n')
