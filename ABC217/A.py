from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
s,t = map(str,input().split())

if s<t:
    print('Yes')
else:
    print('No')