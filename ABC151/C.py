from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,m = map(int,input().split())
A = [0]*n
B = [0]*n
a,w = 0,0
for _ in range(m):
    p,s = map(str,input().split())
    p = int(p)-1
    if A[p]==1:
        continue
    else:
        if s=='AC':
            A[p] = 1
            a += 1
        else:
            B[p]+=1
for i in range(n):
    if A[i]==1:
        w += B[i]
print(a,w)
