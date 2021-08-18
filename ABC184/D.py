from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
from functools import lru_cache
INF = float('inf')
a,b,c = map(int,input().split())
@lru_cache(maxsize=None)
def helper(a,b,c):
    all = a+b+c
    if a==100 or b==100 or c==100:
        return 0
    return 1+ (a*helper(a+1,b,c) + b*helper(a,b+1,c) + c*helper(a,b,c+1))/all

print(helper(a,b,c))