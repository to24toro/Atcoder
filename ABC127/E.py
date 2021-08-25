from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,m,k = map(int,input().split())

mod = 10**9+7


frac = [1]*(n*m+1)
finv = [1]*(n*m+1)
for i in range(n*m):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n*m+1):
    finv[n*m-i] = finv[n*m-i+1]*(n*m-i+1)%mod
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]*finv[n-r]*finv[r]%mod
ans = 0
for d in range(m+1):
    ans +=n*n%mod*d*(m-d)%mod
for d in range(n+1):
    ans +=m*m%mod*d*(n-d)%mod
print(nCr(m*n-2,k-2)*ans%mod)