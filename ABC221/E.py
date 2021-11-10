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
mod= 998244353
L = array('i',[])
L.append(A[-1])
p2 = [1]
ans = 0
for i in range(4*10**5):
    p2.append(p2[-1]*2%mod)
for i in range(n-2,-1,-1):
    idx = bisect_left(L,A[i])
    if idx ==len(L):
        L.append(A[i])
        continue
    ans += p2[n-i-idx-1]-1
    # print(idx,A[i])
    # print(L,ans,p2[n-i-idx-1],n-i-idx-1)
    insort_left(L,A[i])
print(ans)
# print(L)
# print(sorted(A))