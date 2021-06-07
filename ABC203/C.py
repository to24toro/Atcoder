from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,k = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
L.sort()
cnt = k
i = 0
s = 0
while i<n and cnt>0:
    a,b = L[i]
    if a-s<=k:
        k-=a-s
        k+=b
        i += 1
        s = a
    else:
        s +=k
        print(s);exit()
if k:
    s+=k
print(s)
