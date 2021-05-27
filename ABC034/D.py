from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,k = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
l,r = 0,100
while r-l>10**(-9):
    mid = (l+r)/2
    s = [L[i][0]*(L[i][1]-mid) for i in range(n)]
    s.sort(reverse=True)
    if sum(s[:k])>=0:
        l = mid
    else:
        r = mid
print(l)

