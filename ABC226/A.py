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
x = input()
m = int(x[-3])
if m>4:
    print(int(float(x))+1)
else:
    print(int(float(x)))