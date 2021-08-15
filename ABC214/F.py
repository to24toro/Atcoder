from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
mod = 10**9+7

S = input()
n = len(S)
dp = [0]*(n+2)
dp[0] = 1
for i in range(n):
    for j in range(-1,i)[::-1]:
        dp[i+2] += dp[j+1]
        dp[i+2]%=mod
        if j==-1 or S[j]==S[i]:
            break
ans = 0
for i in range(2,n+2):
    ans += dp[i]
    ans %=mod
print(ans)