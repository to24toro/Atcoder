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
n = int(input())
S = list(input())
q = int(input())
f = 0
for _ in range(q):
    t,a,b = map(int,input().split())
    if t==2:
        f = 1-f
    else:
        a-=1;b-=1
        if f==1:
            a = (a+n)%(2*n)
            b = (b+n)%(2*n)
        S[a],S[b] = S[b],S[a]
print("".join(S) if f==0 else "".join(S[n:]+S[:n]))
            