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
n = int(input())
ans = 0
for i in range(1,n):
    ans += (n-1)//i
print(ans)
