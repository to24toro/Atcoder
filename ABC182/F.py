from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import numpy as np
from functools import lru_cache
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7

n,x = map(int,input().split())
A = list(map(int,input().split()))

memo = defaultdict(int)

@lru_cache(None)
def f(X,i):
    if i==n-1:
        return 1*(X>=0)
    a,b = A[i],A[i+1]
    assert X%a == 0
    if X%b==0:
        return f(X,i+1)
    X-=X%b
    return f(X,i+1) + f(X+b,i+1)
print(f(x,0))
