from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

MOD = 10**9+7
x,a = map(int,input().split())
if x<a:
    print(0)
else:
    print(10)