from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

h,w,c = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]

def helper(h,w,a):
    da = [[0]*w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1,w):
        da[0][i] = min(da[0][i-1],a[0][i])
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            cnt_w = a[i][j]
            da[i][j] = min(da[i-1][j],cnt_w)
    return da
ans = INF
for _ in range(2):
    AA = [[0]*w for _ in range(h)]
    for i in range(1,h+1):
        for j in range(1,w+1):
            AA[i-1][j-1] =A[i-1][j-1] - c*(i+j)
    da = helper(h,w,AA)
    # print(da)
    for i in range(h):
        for j in range(w):
            if i==0 and j ==0:
                continue
            elif i==0:
                ad = da[i][j-1]
            elif j ==0:
                ad = da[i-1][j]
            else:
                ad = min(da[i][j-1],da[i-1][j])
            # print(A[i][j]+c*(i+j+2),ad)
            ans = min(ans,A[i][j]+c*(i+j+2) +ad)
    A.reverse()
print(ans)