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
s = A[0]
ans,r = 0,1
for l in range(n):
    while r<n and s + A[r] ==s^A[r]: ##ここに条件かく
        s += A[r]
        r += 1
    ans +=r-l
    s-=A[l]
print(ans)