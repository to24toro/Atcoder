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

n,k = map(int,input().split())
L = [tuple(map(int,input().split())) for _ in range(k)]
L.sort(key = lambda x:x[0])
dp = [0]*(n+1)
S = [0]*(n+1)
dp[1]=1
for i in range(1,n+1):
    for j in range(k):
        l,r = L[j]
        rr = max(i-l,0)
        ll = max(i-r-1,0)
        dp[i]+=S[rr]-S[ll]
        dp[i]%=MOD
    S[i] = S[i-1]+dp[i]
    S[i]%=MOD
    # print(S)
print(dp[-1]%MOD)

