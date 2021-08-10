from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
a,b = map(int,input().split())
for c in range(256):
    if a^c==b:
        print(c);exit()