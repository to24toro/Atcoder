from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,x = map(int,input().split())
s = input()
for i in s:
    if i=='o':
        x +=1
    else:
        x = max(0,x-1)
print(x)