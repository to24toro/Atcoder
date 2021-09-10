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
n,k = map(int,input().split())

L = []
for _ in range(k):
    l,r = map(int,input().split())
    L.append((l,r))
memo = defaultdict(int)
MOD = 998244353
dp = [0]*(2*n+10)
A = [0]*(2*n+10)
dp[0] = 1
A[1] = 1
for i in range(1,n+1):
    for l,r in L:
        l = max(0,i-l+1)
        r = max(i-r,0)
        dp[i] += A[l]-A[r]
        dp[i] %=MOD
    A[i+1] = A[i]+dp[i]

# print(*dp[:7])
print(dp[n-1])