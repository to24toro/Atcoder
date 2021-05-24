from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

a,b,k = map(int,input().split())
n = a+b
frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]//frac[n-r]//frac[r]

def dfs(s,aa,bb,kk):
    if len(s)==n:
        return s
    if aa==0:
        return s+'b'*bb
    elif bb ==0:
        return s+'a'*aa
    else:
        tmp = nCr(aa+bb-1,bb)
        if tmp>=kk:
            return dfs(s+'a',aa-1,bb,kk)
        else:
            return dfs(s+'b',aa,bb-1,kk-tmp)
print(dfs("",a,b,k))
