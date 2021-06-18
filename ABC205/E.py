from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
mod = 10**9+7
n,m,k = map(int,input().split())
frac = [1]*(n+m+1)
finv = [1]*(n+m+1)
for i in range(n+m):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+m+1):
    finv[n+m-i] = finv[n+m-i+1]*(n+m-i+1)%mod
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]*finv[n-r]*finv[r]%mod
if k<n-m:
    print(0);exit()
ans = nCr(n+m,m)
# print(ans)

for i in range(1,n+1):
    p = (k+i)//2
    if i%2:
        for j in range(p+1,n+1):
            # print(i,j,nCr(i,j),nCr(n+m-i,j-n))
            ans += nCr(i,j)*nCr(n+m-i,j-n)
            ans%=mod
    else:
        for j in range(p+1,n+1):
            ans -= nCr(i,j)*nCr(n+m-i,j-n)
            ans%=mod
    # print(i,p,ans,k)
print(ans)


