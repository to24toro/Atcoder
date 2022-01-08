from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
N = int(input())
L=[]
for _ in range(N):
    L.append(input())
 
print(len(list(set(L))))