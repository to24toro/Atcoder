from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import numpy as np
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

n = int(input())
A = list(map(int,input().split()))
dp = dp(2*n,2*n,INF)
for i in range(2*n-1):
    dp[i][i+1] = abs(A[i]-A[i+1])

for i in range(1,2*n,2):
    for j in range(2*n-i):
        l = j
        r = i+ j
        for k in range(l,r):
            dp[l][r] = min(dp[l][r],dp[l][k]+dp[k+1][r])
        dp[l][r] = min(dp[l][r],dp[l+1][r-1] + abs(A[l]-A[r]))
print(dp[0][-1])