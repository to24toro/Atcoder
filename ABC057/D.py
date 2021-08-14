from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,a,b = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
def c(n,k): 
  if(k<=0 or n<=k):
  	return 1
  else:
  	return(c(n-1, k-1) + c(n-1, k))
print(sum(A[:a])/a)
p = A[a-1]
if p !=A[a]:
    print(1);exit()
else:
    x = 0
    y = 0
    for i in range(a-1,-1,-1):
        if p ==A[i]:
            x += 1
    for i in range(a,n):
        if p==A[i]:
            y += 1
    print(c(x+y,x))
    
