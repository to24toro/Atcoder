from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

a,b,x = map(int,input().split())

l,r = 0,min(x+1,10**9+1)
while r-l>1:
    m = (r+l)//2
    cost = a*m+b*int(len(str(m)))
    if cost<=x:
        l = m
    else:
        r = m
print(l)