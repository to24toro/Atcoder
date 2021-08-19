from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

h,w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]
B = [list(map(int,input().split())) for _ in range(h)]

S = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        S[i][j] = abs(A[i][j]-B[i][j])
n = 161*81
dp = [[[False]*n for _ in range(w)] for _ in range(h)]
dp[0][0][S[0][0]] = True
for i in range(h):
    for j in range(w):
        for k in range(n):
            if dp[i][j][k]:
                if i<h-1:
                    dp[i+1][j][abs(k-S[i+1][j])] = dp[i][j][k]
                    dp[i+1][j][(k+S[i+1][j])] = dp[i][j][k]
                if j<w-1:
                    dp[i][j+1][abs(k-S[i][j+1])] = dp[i][j][k]
                    dp[i][j+1][(k+S[i][j+1])] = dp[i][j][k]
# print(dp[-2][-1][:10])
for k in range(n):
    if dp[-1][-1][k]:
        print(k);exit()

