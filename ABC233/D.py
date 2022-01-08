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
n,k = map(int,input().split())
A = list(map(int,input().split()))
S = [0] + list(accumulate(A))
d = Counter(S)
ans = 0
for s in S:
    t = s + k
    d[s]-=1
    if d[t]:
        ans += d[t]
print(ans)