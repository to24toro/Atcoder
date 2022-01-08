from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,X = map(int,input().split())
g = []
ans = 0
for _ in range(n):
    l = list(map(int,input().split()))
    g.append(l[1:])
# print(g)
def rec(i,cur):
    global ans
    if cur>X:
        return
    if i==n:
        if cur==X:ans += 1
        return
    L = g[i]
    for j in range(len(L)):
        rec(i+1,cur*L[j])
    return
rec(0,1)
print(ans)
