from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
k,x = map(int,input().split())
if 500*k>=x:
    print('Yes')
else:
    print('No')