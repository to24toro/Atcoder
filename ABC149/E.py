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
n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
S = [0]+list(accumulate(A))
ans = 0
ng,ok = 0,max(A)*2+1
# print(A)
while ok -ng>1:
    mid = (ok+ng)//2
    cnt = 0
    for a in A:
        b = mid-a
        idx = bisect_left(A,b)
        # print(a,idx,b)
        cnt += n-idx
    if cnt >=m:
        ng = mid
    else:
        ok = mid
cnt = 0
for a in A:
    b = ng-a
    idx = bisect_left(A,b)
    cnt += n-idx
    ans += S[-1]-S[idx] + a*(n-idx)
ans-=ng*(cnt-m)
print(ans)

