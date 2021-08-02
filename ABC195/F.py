from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
<<<<<<< HEAD
INF = float('inf')
=======
INF = float('inf')

A,B = map(int,input().split())
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
n = len(L)
dp = [0]*2**n

dp[0]=1

for i in range(A,B+1):
    ret = 0
    for j in range(n):
        if i%L[j]==0:
            ret |= (1<<j)
    for j in range(2**n):
        if ret&j:
            continue
        dp[j|ret] += dp[j]
print(sum(dp))



>>>>>>> 06f3b92c3ced612344c5c213a76a13a72189e505
