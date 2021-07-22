from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
s = input()
a = s[:n//2]
b = s[n//2:]
if n%2:
    print('No')
else:
    if a==b:
        print('Yes')
    else:
        print('No')