from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
t= int(input())
A = []
for _ in range(t):
    a,b,c = map(int,input().split())
    ans = 0
    d = min(b//2,c)
    ans += d
    b,c = b-d*2,c-d
    d = min(c//2,a)
    ans += d

    a,c = a-d,c-2*d
    ans += min(a,b)//2
    a,b = a-min(a,b),b-min(a,b)
    a += c//2
    ans += a//5
    A.append(ans)

for a in A:
    print(a)
