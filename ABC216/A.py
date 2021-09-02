from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

x = float(input())
y =int(str(x)[-1])
x = str(x)[:-2]
if 0<=y<=2:
    print(x+'-')
elif 3<=y<=6:
    print(x)
else:
    print(x+'+')