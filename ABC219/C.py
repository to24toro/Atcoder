from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
X = [x for x in input()]
n = int(input())
S = [input() for _ in range(n)]
ans = defaultdict(str)
dic = defaultdict(int)
for i,x in enumerate(X):
    dic[x]=i+1
T = []
for s in S:
    p = tuple(dic[i] for i in s)
    T.append(p)
    ans[p] = s
T.sort()
for t in T:
    print(ans[t])