from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,k = map(int,input().split())
A = list(map(int,input().split()))
S = [0]+list(accumulate(A))
ans = 0
for i in range(n):
    s = S[i]
    idx = bisect_left(S,s+k)
    ans +=max(0,n-idx+1)
print(ans)