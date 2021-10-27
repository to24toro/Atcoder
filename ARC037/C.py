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
B = list(map(int,input().split()))
A.sort()
B.sort()

r = A[-1]*B[-1]
l = A[0]*B[0]-1
while r-l>1:
    m = (r+l)//2
    cnt = 0
    for a in A:
        n = m/a
        idx = bisect_right(B,n)
        cnt += idx
    print(r,l)
    if cnt<k:
        l = m
    else:
        r = m
print(r)