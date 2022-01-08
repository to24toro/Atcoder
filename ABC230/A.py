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
n = int(input())
if n<10:
    print("AGC00"+str(n))
elif n>=42:
    print("AGC0"+str(n+1))
else:
    print("AGC0"+str(n))
