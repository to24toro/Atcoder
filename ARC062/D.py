from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

s = input()
cost = 0
g = 0
p = 0

for i in s:
    if i=='g':
        if g==p:
            g += 1
        else:
            p+=1
            cost += 1
    else:
        if g==p:
            g += 1
            cost-=1
        else:
            p += 1
print(cost)
