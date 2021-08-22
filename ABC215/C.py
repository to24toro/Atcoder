from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
s,k = input().split()
k = int(k)
L = list(range(len(s)))
ans = set()
for l in permutations(L):
    ll = list(l)
    res = []
    for i in ll:
        res.append(s[i])
    
    ans.add("".join(res))
ans = sorted(list(ans))
print(ans[k-1])