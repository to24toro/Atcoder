from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for b in B:
    idc = bisect_right(C,b)
    if idc==n:
        continue
    ida = bisect_left(A,b)
    if ida==0:
        continue
    ans += (n-idc)*(ida)
print(ans)
