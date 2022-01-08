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
s = input()
set_ = set()
for i,j,k in permutations([0,1,2]):
    set_.add(s[i]+s[j]+s[k])
print(len(set_))
