from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
p = float(input())
ans = INF
P = p
l,r = 0,150

while r-l>1e-8:
    rr = (2*r+l)/3
    ll = (2*l+r)/3
    R = rr + P/pow(2,rr/1.5)
    L = ll + P/pow(2,ll/1.5)
    if L<R:
        r = rr
    else:
        l = ll
print(r+P/pow(2,r/1.5))
