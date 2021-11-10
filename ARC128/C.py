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
n,m,s = map(int,input().split())
A = list(map(int,input().split()))
S = [0]+list(accumulate(A))
ans=0
for i in range(n+1):
    if s<m*i:break
    x=m*(S[-1]-S[n-i])
    p=0
    for j in range(n-i,0,-1):
        y=(s-m*i)/j
        if m<y:break
        p=max(p,y*(S[n-i]-S[n-i-j]))
    ans=max(ans,x+p)
print(ans)
# ans = 0
# pre = m
# end = n
# for _ in range(5000):
#     max_=-INF
#     # for i,a in enumerate(A[:end]):
#     #     if max_<=a:
#     #         max_=a
#     #         idx = i
    
#     sum_ = S[end]-S[end-1]
#     cnt = 1
#     ii = end-1
#     idx = end-1
#     for j in range(ii-1,-1,-1):
#         if cnt*A[j]>=sum_:
#             cnt += 1
#             sum_+=A[j]
#             idx-=1
#         else:
#             break
#     xi = s/cnt
#     # print(cnt,s,xi)
#     if xi<=m:
#         ans +=(S[end]-S[idx])*xi
#         print(ans);exit()
#     else:
#         xi = m
#         s-=xi*cnt
#         ans +=(S[end]-S[idx])*xi
#         end = idx
#         m = xi
    
