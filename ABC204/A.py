from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

x,y = map(int,input().split())
if x==y:
    print(x)
else:
    print(3-x-y)