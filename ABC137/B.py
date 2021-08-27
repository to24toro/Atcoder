from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
k,x = map(int,input().split())
ans = []
for i in range(max(-1000000,x-k+1),min(x+k-1,1000000)+1):
    ans.append(i)
print(*ans)