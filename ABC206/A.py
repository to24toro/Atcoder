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
n = int(1.08*n)
if n<206:
    print('Yay!')
elif n>206:
    print(':(')
else:
    print('so-so')