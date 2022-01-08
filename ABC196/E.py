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

n = int(input())
min_ = -INF
max_ = INF
b = 0
for _ in range(n):
    a,t = map(int,input().split())
    if t ==1:
        b += a
        min_ += a
        max_ += a
    elif t == 2:
        max_ = max(a,max_)
        min_ = max(a,min_)
    else:
        max_ = min(a,max_)
        min_ = min(a,min_)

q = int(input())
X = list(map(int,input().split()))
for x in X:
    min_x = min_-b
    max_x = max_-b
    if min_ == max_:
        print(min_)
    elif min_x>x:
        print(min_)
    elif max_x<x:
        print(max_)
    else:
        print(x+b)

