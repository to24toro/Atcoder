from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,k = map(int,input().split())
A = list(map(int,input().split()))
s = A[0]
for a in A[1:]:
    s = math.gcd(s,a)

ok,ng = 0,10**19
while ng-ok>1:
    m = (2*ok+ng)//3
    n = (ok+2*ng)//3
    cnt1 = 0
    cnt2 = 0
    for a in A:
        cnt1 += (m-a%m)%m
        cnt2 += (n-a%n)%n
    if cnt1>cnt2:
        ok = cnt1
    else:
        ng = cnt2
    print(cnt,m)
print(max(s,ok))

