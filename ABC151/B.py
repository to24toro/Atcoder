from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,k,m = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)
d = n*m-s
if d>k:
    print(-1)
else:
    print(max(0,d))