from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
<<<<<<< HEAD
from functools import lru_cache

sys.setrecursionlimit(1<<20)
INF = float('inf')

N = int(input())
S = list(map(int,input().split()))
X = input()

T = []
@lru_cache(None)
def dp(i,j):
    if i==0:
        pass
    m = S[i]
    tmp = (pow(10,N-1-i,7)*m + j)%7
    if X[i]=='A':
        return dp(i-1,j) & dp(i-1,tmp)

print(dp(N-1,0))
=======
sys.setrecursionlimit(1<<20)
INF = float('inf')
>>>>>>> 06f3b92c3ced612344c5c213a76a13a72189e505
