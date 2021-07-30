from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
mod = 10**9+7

n = int(input())
A = list(map(int,input().split()))
if n==1:
    print(1)
    print(1)
    exit()
if n==2:
    print(2)
    if A[0]==A[-1]:
        print(3)
    else:
        print(2)
    print(1)
    exit()
print(n)
frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+1):
    finv[n-i] = finv[n-i+1]*(n-i+1)%mod
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]*finv[n-r]*finv[r]%mod
dic = defaultdict(int)
for i in range(n+1):
    if A[i] not in dic:
        dic[A[i]] = i
    else:
        j = i-dic[A[i]]-1
for k in range(2,n+2):
    ans = 0
    ans +=nCr(n-1,k-2)
    ans %=mod
    ans += nCr(n-1,k)
    ans %=mod
    ans += 2*nCr(n-1,k-1)
    ans %=mod
    ans -=nCr(n-j-1,k-1)
    ans %=mod
    print(ans)