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
X = list(input())
L = [int(x) for x in X]
S = list(accumulate(L))
n = len(X)
ans = [0]*n
pre = 0
for i in range(n):
    cur = S[n-i-1]+pre
    res = cur%10
    pre = cur//10
    ans[n-i-1] = res
ans2 = [str(a) for a in ans]
ans1 =""
if pre:
    ans1 = str(pre)

print(ans1+"".join(ans2))