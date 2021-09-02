from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
a,b,c,d = map(int,input().split())
g = math.gcd(c,d)
e = c*d//g
cc = b//c -(a-1)//c
dd = b//d -(a-1)//d
ee = b//e-(a-1)//e
# print(cc,dd,e)
f = cc+dd-ee
print(b-a-f+1)