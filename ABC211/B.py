from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
s = set()
for _ in range(4):
    a = input()
    s.add(a)
if len(s)==4:
    print('Yes')
else:
    print('No')