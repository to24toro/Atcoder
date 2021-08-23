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
ans =0
for i in range(1,n):
    ans += max(0,A[i-1]-A[i])
    A[i] = max(A[i-1],A[i])
print(ans)