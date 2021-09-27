from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
a,b,c = map(int,input().split())
for i in range(a,b+1):
    if i%c==0:
        print(i);exit()
print(-1)