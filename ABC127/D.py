from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,m = map(int,input().split())
A = list(map(int,input().split()))
ans = sum(A)
A.sort()
S = list(accumulate(A))
# print(S)
B = []
L = []
for _ in range(m):
    b,c = map(int,input().split())
    L.append((b,c))
L.sort(reverse=True)
f =False
cnt = 0
for b,c in L:
    for i in range(b):
        cnt+=1
        B.append(c)
        if cnt==n:
            f =True
            break
    if f:
        break
C = A+B
C.sort(reverse=True)
print(sum(C[:n]))
    