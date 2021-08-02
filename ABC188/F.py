from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
X,Y = map(int,input().split())
# print('AAAAAA')
memo = defaultdict(int)
memo[0] = X
def dp(y):
    res = 0
    if memo[y]:
        return memo[y]
    if y<X:
        return X-y
    if y ==X:
        return res
    if y%2:
        if (y+1)//2>=X:
            res = min(2 + dp((y+1)//2),2 + dp((y-1)//2))
        else:
            res = min(y-X,2+dp((y+1)//2),2+dp((y-1)//2))
    else:
        if y//2>=X:
            res = 1+dp(y//2)
        else:
            res = min(y-X,dp(y//2)+1)
    memo[y] = res
    return memo[y]

print(dp(Y))