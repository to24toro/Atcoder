from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    for j in range(1,k+1):
        ans += 100*i+j
print(ans)