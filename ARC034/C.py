import collections
from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
mod = 10**9+7
a,b = map(int,input().split())
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
dic = defaultdict(int)
for i in range(b+1,a+1):
    a = prime_factorize(i)
    for j in a:
        dic[j]+=1
ans = 1
for k,v in dic.items():
    ans *= (v+1)
    ans%=mod
print(ans)