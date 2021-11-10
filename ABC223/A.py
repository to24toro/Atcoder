from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
A,B,C = [],[],[]
for a,b in L:
    A.append(a)
    B.append(a/b)
    C.append(b)

S = [0]+list(accumulate(A))
SB = [0]+list(accumulate(B))
l,r = 0,S[-1]+1
while r-l>1e-8:
    m = (r+l)/2

    idx = bisect_left(S,m)
    t1 = SB[idx-1]
    t2 = SB[-1]-SB[idx]
    b = C[idx-1]
    t1 += (m-S[idx-1])/b
    t2 += (S[idx]-m)/b
    if abs(t1-t2)<1e-7:
        print(m)
        exit()
    else:
        if t1>t2:
            r = m
        else:
            l = m
