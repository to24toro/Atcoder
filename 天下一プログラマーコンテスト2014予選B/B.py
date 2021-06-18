from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

N = int(input())
S = input()
T = [input() for _ in range (N)]
mod = 1000000007
l = len(S)
dp = [0]*(l+1)
dp[0]=1
for i in range (l):
    for t in T:
        if i+len(t)<=l:
            if S[i:i+len(t)]==t:
                dp[i+len(t)]+=dp[i]
                dp[i+len(t)]%=mod
print(dp[-1])  