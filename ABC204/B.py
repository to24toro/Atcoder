from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = list(map(int,input().split()))
ans = 0
for a in A:
    if a>10:
        ans += a-10
print(ans)