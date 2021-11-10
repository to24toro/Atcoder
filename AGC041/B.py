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

n,m,v,p = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
def helper(x):
    if A[x-1]+m<A[p-1]:
        return False
    else:
        rest = m*(v-(p-1)-(n-x+1))
        if rest>0:
            for i in range(p-1,x-1):
                rest-=A[x-1]+m-A[i]
            return rest<=0
        else:
            return True
l,r = 0,n+1
while r-l>1:
    mid = (r+l)//2
    if helper(mid):
        l = mid
    else:
        r = mid
print(l)