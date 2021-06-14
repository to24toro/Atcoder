from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

n//=2
c = []
d = []
for i in range(2*n):
    if i%2:
        c.append(b[i]-a[i])
    else:
        d.append(b[i]-a[i])
ans = sum(a)
c.sort(reverse=True)
d.sort(reverse=True)
for i in range(n):
    if c[i]+d[i]>0:
        ans += c[i]+d[i]
print(ans)