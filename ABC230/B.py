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
s = input()
T = "oxx"*200
for i in range(180):
    t = T[i:i+len(s)]

    if s==t:
        print('Yes');exit()
print('No')