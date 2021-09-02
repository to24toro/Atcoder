from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

R,B = map(int,input().split())
x,y = map(int,input().split())
if x==1 or y==1:
    print(min(R,B));exit()
l,r = 0,10**18+1
while (r-l)>1:
    m = (r+l)//2
    rr = R-m
    bb = B-m
    if rr<0 or bb<0:
        r = m
    else:
        chk = (rr//(x-1)) + (bb//(y-1))
        if chk>=m:
            l =m
        else:
            r = m
print(l)