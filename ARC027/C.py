from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

x,y = map(int,input().split())
n = int(input())
L =[list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(x+y+1) for _ in range(x+1)]

for i in range(1,n+1):
    t,h = L[i-1]
    for j in reversed(range(1,x+1)):
        for k in reversed(range(x+y+1)):
            if k-t>=0:
                dp[j][k] = max(dp[j-1][k-t]+h,dp[j][k],dp[j][k])
            else:
                dp[j][k] = max(dp[j][k],dp[j][k])
# ans = 0
print(max(dp[-1]))