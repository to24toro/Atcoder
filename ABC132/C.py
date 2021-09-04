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
D = list(map(int,input().split()))
D.sort()
d1 = D[n//2-1]
d2 = D[n//2]
print(d2-d1)