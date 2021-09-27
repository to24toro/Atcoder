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
A = list(map(int,input().split()))
MOD = 998244353
dp = [[0]*10 for _ in range(n)]
dp[0][A[0]]=1
for i in range(1,n):
    a = A[i]
    for j in range(10):
        dp[i][(j+a)%10]+=dp[i-1][j]
        dp[i][(j*a)%10]+=dp[i-1][j]
        dp[i][(j*a)%10]%=MOD
        dp[i][(j+a)%10]%=MOD
print(*dp[-1],sep = '\n')