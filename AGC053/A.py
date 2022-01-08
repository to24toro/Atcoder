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
S = list(input())
A = list(map(int,input().split()))
d = INF
for i in range(n):
    d = min(d,abs(A[i+1]-A[i]))
print(d)
B = [[0]*(n+1) for _ in range(d)]
for i in range(n+1):
    p = A[i]//d
    for j in range(d):
        B[j][i] +=p
    for j in range(A[i]%d):
        B[j][i] += 1
for i in range(d):
    print(*B[i])
