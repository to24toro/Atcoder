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
s = list(input())
t = list(input())
if s==t:print('Yes');exit()
for i in range(len(s)-1):
    s[i],s[i+1] = s[i+1],s[i]
    if s==t:
        print('Yes');exit()
    s[i],s[i+1] = s[i+1],s[i]
print('No')