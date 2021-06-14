from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

A = list(map(int,input().split()))
set_ = set(A)
if len(set_)==3:
    print(0)
else:
    A.sort()
    if A[0]==A[1]:
        print(A[-1])
    else:
        print(A[0])