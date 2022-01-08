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
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
L = make_divisors(n)[::-1]

m = len(L)
L.append(0)
ans = 0
ll,rr = 1,n
cur = 1
while ll<rr:
    l,r = ll,rr
    while r-l>1:
        m = (r+l)//2
        p = n//m
        if p>cur:
            l = m
        else:
            r = m
    # print(cur,rr,r)
    ans += cur*(rr-r+1)
    cur = n//(r-1)
    rr = r-1

print(ans+n)