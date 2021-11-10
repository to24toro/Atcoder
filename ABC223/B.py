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
x = int(input())
if x%100!=0:
    print('No')
    exit()
if x<100:
    print('No');exit()
print('Yes')