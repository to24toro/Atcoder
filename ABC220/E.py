from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
MOD = 998244353
n,d = map(int,input().split())
p2 = [1]
for i in range(2*10**6+1):
    p2.append(p2[-1]*2%MOD)

ans = 0
for i in range(n):
    if i+d<n:
        ans += p2[d]*p2[i]*2

    l = max(1,d-n+i+1)
    r = min(d-1,n-i-1)
    if l<=r:
        ans += (r-l+1)*p2[d-2]*p2[i]*2
    ans%=MOD
print(ans%MOD)
