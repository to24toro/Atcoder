from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

L.sort(key = lambda x:x[0])
dp = [[0]*5002 for _ in range(n+1)]
for i in range(1,n+1):
    d,c,s = L[i-1]
    for j in range(1,5002):
        dp[i][j] = max(dp[i][j],dp[i-1][j])
        if j+c-1<=d:
            dp[i][j+c] = max(dp[i][j+c],dp[i-1][j]+s)
print(max(dp[-1]))