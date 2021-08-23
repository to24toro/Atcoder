from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,x,t = map(int,input().split())
if n%x==0:
    c = n//x
else:
    c = n//x+1
print(t*c)