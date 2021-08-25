from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
a,b = map(int,input().split())
if a>=13:
    print(b)
elif a<=5:
    print(0)
else:
    print(b//2)