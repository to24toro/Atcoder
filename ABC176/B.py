from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = input()
ans = 0
for i in n:
    ans += int(i)
if ans%9==0:
    print('Yes')
else:
    print('No')