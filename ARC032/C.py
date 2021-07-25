from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
L = []
for i,l in enumerate(A):
    a,b = l
    L.append((a,b,i))
L.sort()
print(L)