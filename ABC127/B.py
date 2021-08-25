from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
r,d,x =map(int,input().split())
for i in range(10):
    print(r*x-d)
    x = r*x-d