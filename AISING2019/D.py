from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
L1=A.copy()
for j in range(n-2,-1,-1):
    L1[j]+=L1[j+1]
 
L2=[0,0]+A.copy()
for i in range(2,n+2):
    L2[i]+=L2[i-2]
S = list(accumulate(A))
for _ in range(q):
    x = int(input())
    l,r = 0,n-1
    while r-l>1:
        m = (r+l)//2
        y = A[m]
        if y<=x:
            l = m
            continue
        diff = y-x
        left = bisect_left(A,x-diff)
        z = m-left+1
        if n-m-1>=z:
            l = m
        else:
            r = m
    # print(left,z,l,r,2*m-n+1)
    print(L2[-(n-r)*2-1]+L1[r])


