from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

h,w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]
ha = [sum(A[i]) for i in range(h)]
hb = [0]*w
for i in range(h):
    for j in range(w):
        hb[j]+=A[i][j]

B = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        B[i][j] = ha[i]+hb[j]-A[i][j]
for i in range(h):
    print(*B[i])