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
P = list(map(int,input().split()))
for i in range(n):
    if P[i] ==1:
        start = i

PP = P+P
Q = PP[start:start+n]
i = start
if Q[1] ==2:
    print(min(i,n-i+2))
else:
    print(min(i+2,n-i))