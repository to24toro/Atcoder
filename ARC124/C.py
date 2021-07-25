from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
import sys
import random
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]

q = set()
q.add(tuple(sorted(A[0])))
for i in range(1,n):
    a,b = A[i]
    nq = set()
    for aa,bb in q:
        aaa = gcd(a,aa)
        bbb = gcd(b,bb)
        nq.add(tuple(sorted([aaa,bbb])))
        aaa = gcd(a,bb)
        bbb = gcd(b,aa)
        nq.add(tuple(sorted([aaa,bbb])))
    q = nq
ans = 1
for a,b in q:
    ans = max(ans,(a*b)//gcd(a,b))
print(ans)