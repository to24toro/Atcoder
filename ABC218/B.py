from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
P = list(map(int,input().split()))
ans = []
for p in P:
    ans.append(chr(ord('a')+p-1))
print(''.join(ans))