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
S = ["".join((sorted(input()))) for _ in range(n)]
ans = 0
cnt = Counter(S)
for k,v in cnt.items():
    ans += v*(v-1)//2

print(ans)