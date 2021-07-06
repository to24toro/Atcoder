from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = []
B = []
ans = 0
for _ in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
if A ==B:
    print(0);exit()
m = 10**10
for a,b in zip(A,B):
    if a==b:
        ans += a
    elif a<b:
        ans += a
    else:
        ans += a
        m = min(m,b)
print(ans-m)
