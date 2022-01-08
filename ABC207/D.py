from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n = int(input())
S = []
sx,sy = 0,0
tx,ty = 0,0
T = []
for _ in range(n):
    a,b = map(int,input().split())
    sx += a
    sy += b
    S.append([a,b])
for _ in range(n):
    a,b = map(int,input().split())
    tx += a
    ty += b
    T.append([a,b])
sx /= n;sy/=n;tx/=n;ty/=n
for i in range(n):
    S[i][0]-=sx
    S[i][1]-=sy
for i in range(n):
    T[i][0]-=tx
    T[i][1]-=ty

ans = 'No'
eps = 1e-6
for i in range(n)
