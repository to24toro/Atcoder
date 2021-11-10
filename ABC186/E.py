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
def make_divisors(n):
    D = set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            D.add(i)
            if i != n // i:
                D.add(n//i)
        i += 1
    return D
t = int(input())
for _ in range(t):
    n,s,k = map(int,input().split())
    L = make_divisors(n)
    if k in L:
        print(-1)
    else:
        
