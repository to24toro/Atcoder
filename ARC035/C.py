from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m = map(int,input().split())
dp = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    dp[a][b] = c
    dp[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k][j])
k = int(input())
ANS = []
for _ in range(k):
    ans = 0
    x,y,z = map(int,input().split())
    x-=1
    y-=1
    for i in range(n):
        for j in range(i+1,n):
            dp[i][j] = min(dp[i][j],dp[i][x] + dp[y][j] + z,dp[i][y] + dp[x][j] + z)
            dp[j][i] = dp[i][j]
            ans += dp[i][j]
    ANS.append(ans)
print(*ANS,sep = '\n')