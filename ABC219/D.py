from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
X,Y = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
dp = [[n+2]*(Y+1) for _ in range (X+1)]
dp[0][0] = 0
for i in range(n):
    a,b = L[i]
    for j in range(X,-1,-1):
        for k in range(Y,-1,-1):
            dp[min(X,j+a)][min(Y,k+b)] = min(dp[j][k]+1,dp[min(X,j+a)][min(Y,k+b)])
print(dp[-1][-1] if dp[-1][-1]<n+1 else -1)
