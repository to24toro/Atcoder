from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

n = int(input())
A = list(map(int,input().split()))
A.sort()
q = int(input())

for i in range(q):
    b = int(input())
    idx = bisect_left(A,b)
    if idx==n:
        print(abs(b-A[idx-1]))
    else:
        print(min(abs(b-A[idx]),abs(b-A[idx-1])))