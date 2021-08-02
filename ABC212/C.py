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
B = list(map(int,input().split()))
A.sort()
B.sort()
ans = INF
for a in A:
    i = bisect_left(B,a)
    if i==m:
        ans = min(ans,abs(a-B[i-1]))
    else:
        ans = min(ans,abs(a-B[i]),abs(a-B[i-1]))
print(ans)
