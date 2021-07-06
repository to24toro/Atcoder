from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
X = [tuple(map(int,input().split())) for _ in range(n)]

l,r = 0,10**18+1

while r-l>1:
    m = (r+l)//2
    t = 0
    f = True
    T = []
    for h,s in X:
        T.append((m-h)//s)
    T.sort()
    for i,t in enumerate(T):
        if t<0:
            f = False
            break
        if i>t:
            f = False
            break 
    if not f:
        l = m
    else:
        r = m
print(r)
