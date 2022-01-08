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
A.sort()
m = max(A)
S = [0] + list(accumulate(A))
for x in range(1,m):
    prev = 0
    cur = x
    need = 0
    while True:
        idx = bisect_right(A,cur)
        need += cur*(idx-prev)-(S[idx]-S[prev])
        if idx==n:break
        prev = idx
        cur += x
    if need<=k:
        ans = x
ans1 = (k+sum(A))//n
if ans1>=m:
    ans = ans1
print(ans)