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
l = list(input())
n = len(l)
ans = -float('inf')
for i in range(1<<n):
    a,b = [],[]
    for j in range(n):
        if (i>>j)&1:
            a.append((l[j]))
        else:
            b.append((l[j]))
    if not a or not b:
        continue
    a.sort(reverse=True)
    b.sort(reverse=True)
    if a[0]=="0" or b[0]=="0":
        continue
    A = int("".join(a))
    B = int("".join(b))
    ans = max(ans,A*B)
print(ans)