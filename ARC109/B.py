from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
l,r = 0,10**18
while r-l>1:
    m = (r+l)//2
    if m*(m+1)//2<=n+1:
        l = m
    else:
        r = m
print(1+n-l)