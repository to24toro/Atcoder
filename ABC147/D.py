from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
mod = 10**9+7
INF = float('inf')
n = int(input())
A = list(map(int,input().split()))
ans = 0
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
X = [Base_10_to_n(a,2) for a in A]
dp = [[0,0] for _ in range(60)]
for x in X:
    x = x[::-1]
    for i in range(len(x)):
        dp[i][int(x[i])] +=1
    for i in range(len(x),60):
        dp[i][0] += 1
# print(*dp)
for i in range(60):
    ans += dp[i][0]*dp[i][1]*pow(2,i,mod)
    ans %= mod
print(ans)