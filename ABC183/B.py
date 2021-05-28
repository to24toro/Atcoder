from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

a,b,c,d = map(int,input().split())
x = a*d+b*c
y = b+d
print(x/y)