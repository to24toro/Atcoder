from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
h,w,n = map(int,input().split())
H = set()
W = set()
A = []
for _ in range(n):
    a,b = map(int,input().split())
    H.add(a)
    W.add(b)
    A.append((a,b))
H = sorted(list(H))
W = sorted(list(W))
dh = {}
dw = {}
for i in range(1,len(H)+1):
    dh[H[i-1]] = i
for i in range(1,len(W)+1):
    dw[W[i-1]] = i
for a,b in A:
    print(dh[a],dw[b])