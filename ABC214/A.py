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
if 1<=n<=125:
    print(4)
elif 126<=n<=211:
    print(6)
else:
    print(8)