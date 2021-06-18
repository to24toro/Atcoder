from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,x = map(int,input().split())
A = list(map(int,input().split()))

dp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        tmp = A[i]+j*x
        dp[(i+j)%n][i]=tmp
print(dp)