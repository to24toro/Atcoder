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
A = list(map(int,input().split()))
B = [0]*n
C = [0]*n
bb,cc =0,0
if A[0]>0:
    B[0] = A[0]
    bb = A[0]
if A[0]<0:
    C[0] = A[0]
    cc = A[0]

for i in range(n-1):
    B[i+1] = bb
    C[i+1] = cc
    s = B[i+1] + C[i+1]
    if s<A[i+1]:
        B[i+1]+=A[i+1]-s
        bb = B[i+1]
    if s>A[i+1]:
        C[i+1]+=A[i+1]-s
        cc = C[i+1]
D = []
for i in range(n):
    D.append(abs(B[i]))
    D.append(abs(C[i]))
D.sort()
m = D[n]
ans = 0
for i in range(n):
    ans += abs(B[i]-m)+abs(C[i]+m)
print(ans)