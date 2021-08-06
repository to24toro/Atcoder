from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,m = map(int,input().split())
nn = n
C = []
for _ in range(m):
    a,c = map(int,input().split())
    C.append((c,a))
from math import *
C.sort(reverse=True)
nnn = n
ans = 0
c,a = C.pop()
ans = (n-gcd(n,a))*c
res = n-gcd(n,a)
n = gcd(n,a)
# print(res,ans,n)
while n!=1 and C:
    c,a = C.pop()
    if gcd(a,n)==1:
        ans += c*(n-1)
        n = 1
        break
    else:
        if n==gcd(n,a):
            continue
        else:
            ans +=c*(n-gcd(n,a))
            res += n-gcd(n,a)
            n = gcd(n,a)
print(ans if n==1 else -1)
