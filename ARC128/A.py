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
p = 0
ans = []
for i in range(n-2):
    if p==0:
        if A[i]>A[i+1]:
            p = 1
            ans.append(1)
        else:
            p = 0
            ans.append(0)
    else:
        if A[i]<A[i+1]:
            p = 0
            ans.append(1)
        else:
            p = 1
            ans.append(0)

if p==0:
    if A[n-2]>A[n-1]:
        ans.append(1)
        ans.append(1)
    else:
        ans.append(0)
        ans.append(0)
else:
    if A[n-2]>A[n-1]:
        ans.append(0)
        ans.append(1)
    else:
        ans.append(1)
        ans.append(0)
print(*ans)