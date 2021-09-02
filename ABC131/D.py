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
L = [list(map(int,input().split())) for _ in range(n)]
L.sort(key = lambda x:x[1])
s = 0
for a,b in L:
    if s<=b-a:
        s +=a
    else:
        print('No');exit()
print('Yes')