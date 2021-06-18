from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]

def da_generate(h,w,a,m):
    da = [[0]*w for j in range(h)]
    da[0][0] = 1 if a[0][0]>=m else 0
    for i in range(1,w):
        da[0][i] = da[0][i-1]+(a[0][i]>=m)
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]>=m
            da[i][j] = da[i-1][j]+cnt_w
    return da
def da_calc(p,q,x,y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y]-da[x][q-1]
    if q == 0:
        return da[x][y]-da[p-1][y]
    return da[x][y]-da[p-1][y]-da[x][q-1]+da[p-1][q-1]

ok,ng = -1,10**9+1
chk = k**2//2+1
while ng-ok>1:
    m = (ng+ok)//2
    da = da_generate(n,n,A,m)
    # print(m,da)
    judge =True
    for i in range(n-k+1):
        for j in range(n-k+1):
            if da_calc(i,j,i+k-1,j+k-1)<chk:
                judge=False
                break
    if judge:
        ok = m
    else:
        ng = m
print(ok)
