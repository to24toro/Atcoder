from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,x,d = map(int,input().split())
if d==0:
    if x==0:
        print(1)
    else:
        print(n+1)
    exit()

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from fractions import gcd

N,X,D = map(int,read().split())

if D == 0:
    if X == 0:
        print(1)
    else:
        print(N+1)
    exit()

g = gcd(X,D)
X //= g; D //= g
if D < 0:
    X,D = -X,-D

def F(d):
    # Xの個数 = d mod Dのとき
    event = []
    for n in range(d,N+1,D):
        # Xがn個
        low = X * n // D + n * (n-1) // 2
        high = X * n // D + n * (N+N-n-1) // 2
        event.append((low,0))
        event.append((high,1))
    event.sort()
    overlap = 0
    left_end = 0
    cnt = 0
    for x,t in event:
        if not t:
            if not overlap:
                left_end = x
            overlap += 1
        else:
            overlap -= 1
            if not overlap:
                cnt += x - left_end + 1
    return cnt

answer = sum(F(d) for d in range(min(D,N+1)))
print(answer)