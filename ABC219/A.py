from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
x = int(input())
if x>=90:
    print('expert')
elif 70<=x<90:
    print(90-x)
elif 40<=x<70:
    print(70-x)
else:
    print(40-x)