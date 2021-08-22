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
ans = 1
for i in range(10000):
    if ans>n:
        print(i-1)
        exit()
    ans*=2