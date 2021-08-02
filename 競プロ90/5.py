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

n,b,K = map(int,input().split())
C = list(map(int,input().split()))
dp = [[0]*b for _ in range(64)]
p10 = [0]*64
for i in range(63):
    p10[i] = pow(10,1<<i,b)
for c in C:
    dp[0][c%b] += 1

for i in range(62):
    for j in range(b):
        for k in range(b):
            nx = (j*p10[i]+k)%b
            dp[i+1][nx] += dp[i][j]*dp[i][k]
            dp[i+1][nx] %= MOD

ANS = [[0]*b for _ in range(64)]
ANS[0][0] = 1
for i in range(62):
    if n&(1<<i):
        for j in range(b):
            for k in range(b):
                nx = (j*p10[i]+k)%b
                ANS[i+1][nx] += ANS[i][j]*dp[i][k]
                ANS[i+1][nx] %= MOD
    else:
        for j in range(b):
            ANS[i+1][j] = ANS[i][j]
print(ANS[62][0]%MOD)