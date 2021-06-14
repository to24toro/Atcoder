from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
N = int(input())
Q = [-1] * N
for i in range(N):
    p = int(input())
    Q[p - 1] = i
k = 1
seq = 1
for i in range(N - 1):
    if Q[i + 1] > Q[i]:
        seq += 1
    else:
        seq = 1
    k = max(k, seq)
print(N-k)