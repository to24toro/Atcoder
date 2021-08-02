from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

h,w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]
H = []
for i in range(h):
    hh = 0
    for j in range(w):
        hh += A[i][j]
    H.append(hh)
W = []
for j in range(w):
    ww = 0
    for i in range(h):
        ww += A[i][j]
    W.append(ww)
B = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        B[i][j] = H[i] + W[j] - A[i][j]

for b in B:
    print(*b)