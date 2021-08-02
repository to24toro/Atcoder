from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

a,b = map(int,input().split())
if a>0 and b>0:
    print('Alloy')
elif a==0:
    print('Silver')
else:
    print('Gold')