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
X = list(map(int,input().split()))
MOD = 10**9+7
P = [1]
ans = 0
q = 1
for i in range(2,n):
    q*=i
    q %=MOD
for i in range(2,n):
    P.append(P[-1]+pow(i,MOD-2,MOD))
for i in range(n-1):
    d = X[i+1]-X[i]
    ans +=d*P[i]
    ans %= MOD
print((ans*q)%MOD)