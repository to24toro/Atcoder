from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
from bisect import bisect_right
 
N, T = map(int, input().split())
A = list(map(int, input().split()))
L = [0]
R = [0]
for x in A[:20]:
    for i in range(len(L)):
        L.append(x + L[i])
for x in A[20:]:
    for i in range(len(R)):
        R.append(x + R[i])
R.sort()

ans = 0
for x in L:
    if x > T:
        continue
    y = R[bisect_right(R, T - x) - 1]
    if ans < x + y:
        ans = x + y

print(ans)