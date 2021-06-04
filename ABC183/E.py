from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

mod = 10**9+7

h,w = map(int,input().split())

S = ["."*(w+1)]+["."+input() for _ in range(h)]
dp = [[[0,0,0,0] for _ in range(w+1)] for _ in range(h+1)]
dp[1][1][0] = 1
dp[1][1][1] = 1
dp[1][1][2] = 1
dp[1][1][3] = 1
# print(S)
for i in range(1,h+1):
    for j in range(1,w+1):
        if i==1 and j==1:
            continue
        if S[i][j]==".":
            dp[i][j][0] = (dp[i-1][j-1][3]+dp[i-1][j][2]+dp[i][j-1][1])%mod
            dp[i][j][1] = (dp[i][j][0]+dp[i][j-1][1])%mod
            dp[i][j][2] = (dp[i][j][0]+dp[i-1][j][2])%mod
            dp[i][j][3] = (dp[i][j][0]+dp[i-1][j-1][3])%mod
        else:
            continue
# print(dp)
print(dp[-1][-1][0]%mod)
