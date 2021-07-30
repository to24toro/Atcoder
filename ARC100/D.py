from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
A = list(map(int,input().split()))
S = list(accumulate(A))
ans = INF
for i in range(1,n-2):
    x = S[i]/2
    idx = bisect_right(S,x)
    if abs(x-S[idx-1])>abs(S[idx]-x):
        a = S[idx]
        b = S[i]-S[idx]
    else:
        a = S[idx-1]
        b = S[i]-S[idx-1]
    y = S[i]+(S[-1]-S[i])/2
    idy = bisect_right(S,y)
    if abs(y-S[idy-1])>abs(S[idy]-y):
        c = S[idy]-S[i]
        d = S[-1]-S[idy]
    else:
        c = S[idy-1]-S[i]
        d = S[-1]-S[idy-1]
    mx = max(a,b,c,d)
    mn = min(a,b,c,d)
    ans = min(ans,mx-mn)
print(ans)