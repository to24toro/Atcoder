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
a,b,c = map(int,input().split())
print('Yes' if a**2+b**2<c**2 else 'No')
