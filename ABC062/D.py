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
A = list(map(int,input().split()))
a = A[:n]
b = A[n:2*n]
c = A[2*n:]
R = [0]*(n+1)
R[0] = sum(c)
c = [-x for x in c]
heapify(a);heapify(c)
L = [0]*(n+1)
L[0] = sum(a)
for i in range(n):
    L[i+1] = L[i]-a[0]
    t = max(heappop(a),b[i])
    heappush(a,t)
    L[i+1]+=t
for i in range(n):
    R[i+1] = R[i]+c[0]
    # print(R[i+1])
    t = min(-heappop(c),b[n-1-i])
    # print(t)
    heappush(c,-t)
    R[i+1]+=t

ans = -INF
# print(L,R)
for i in range(n+1):
    ans = max(ans,L[i]-R[n-i])
print(ans)