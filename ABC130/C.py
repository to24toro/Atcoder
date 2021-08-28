from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
w,h,x,y = map(int,input().split())
ans = 0
if w/2==x and h/2==y:
    ans = 1

print(w*h/2,ans)