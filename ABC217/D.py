from array import *
from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import array
sys.setrecursionlimit(1<<20)
INF = float('inf')
l,q = map(int,input().split())
L = array.array('i',[])
L.append(0)
L.append(l)
for _ in range(q):
    c,x = map(int,input().split())
    if c==1:
        insort_left(L,x)
    else:
        idx = bisect_left(L,x)
        print(L[idx]-L[idx-1])