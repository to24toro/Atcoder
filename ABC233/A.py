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
x,y = map(int,input().split())
if x>=y:print(0)
else:
    if (y-x)%10:
        print((y-x)//10 + 1)
    else:
        print((y-x)//10)