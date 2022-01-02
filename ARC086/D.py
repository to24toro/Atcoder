from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = list(map(int,input().split()))



mn = min(A)
mx = max(A)
idn = A.index(mn)
idx = A.index(mx)
ANS = []
if mn*mx<0:
    if -mn<=mx:
        for i in range(n):
            ANS.append((idx+1,i+1))
            A[i]+=mx
    else:
        for i in range(n):
            ANS.append((idn+1,i+1))
            A[i]+=mn

mn = min(A)
mx = max(A)
idn = A.index(mn)
idx = A.index(mx)
# print(A)
if mx<=0:
    pre = A[-1]
    for i in range(n-2,-1,-1):
        a = A[i]
        if a>pre:
            ANS.append((idn+1,i+1))
            A[i]+=mn
            if mn>A[i]:
                mn = A[i]
                idn = i
        pre = A[i]
else:
    pre = A[0]
    for i in range(1,n):
        a = A[i]
        if a<pre:
            ANS.append((idx+1,i+1))
            A[i]+=mx
            if mx<A[i]:
                mx = A[i]
                idx = i
        pre = A[i]
print(len(ANS))
for i,j in ANS:
    print(i,j)
