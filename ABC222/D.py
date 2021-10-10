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
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
MOD = 998244353
dp = [[0]*3002 for _ in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    a,b = A[i-1],B[i-1]
    S = [dp[i-1][0]]
    for j in range(1,3002):
        S.append((S[-1]+dp[i-1][j])%MOD)
    for j in range(a,b+1):
        dp[i][j] = S[j]
ans = 0
for d in dp[-1]:
    ans += d
    ans %=MOD
print(ans)
    
