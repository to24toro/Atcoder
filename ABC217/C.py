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
P = list(map(int,input().split()))
Q = [0]*n
for i,p in enumerate(P):
    Q[p-1] = i+1
print(*Q)