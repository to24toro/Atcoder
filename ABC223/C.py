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
s = list(input())
n = len(s)
a = []
for i in range(n):
    t = s[i:]+s[:i]
    a.append("".join(t))
a.sort()
print(a[0])
print(a[-1])

