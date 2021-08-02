from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import numpy as np
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]
n = int(input())
if n%2:exit()
for bit in range(1<<n):
    A = []
    cur = 0
    s = 0
    f = True
    ans = ''
    for j in range(n):
        if (1<<j)&bit==0:
            cur-=1
            ans += ')'
        else:
            cur += 1
            s += 1
            ans += '('
        if cur <0:
            f = False
            break
    if s != n//2:
        f = False
    if f:
        print(ans)
