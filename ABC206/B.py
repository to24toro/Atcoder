from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
a =1
s = 0
for i in range(10**9):
    s+=i+1
    if s>=n:
        print(i+1);exit()