from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys

sys.setrecursionlimit(1<<20)
INF = float('inf')
L,R = map(int,input().split())
ans = 0
class MultipleFactorization:
    def __init__(self, n):
        self.n = n
        self.sieve = [i for i in range(n + 1)]
        self._set()
 
    def _set(self):
        i = 2
        while i <= self.n:
            self.sieve[i] = 2
            i += 2
 
        for i in range(3, self.n + 1):
            if self.sieve[i] == i:
                j = i ** 2
                while j <= self.n:
                    if self.sieve[j] == j:
                        self.sieve[j] = i
                    j += i
 
    def factorization(self, x):
        factors = []
        while x > 1:
            k = self.sieve[x]
            factors.append(k)
            x //= k
        return factors
mf = MultipleFactorization(R + 1)

# for i in range(2,R+1):
#     f = mf.factorization(i)
#     l = len(f)
#     if l!=len(set(f)):
#         continue
#     c = (R//i)-((L-1)//i)
#     tmp = c*(c-1)//2
#     if l%2:
#         ans += tmp
#     else:
#         ans-=tmp
#     if i>=max(2,L):
#         ans-=R//i-1
# print(2*ans)
ans = 0
for i in range(2, R + 1):
    f = mf.factorization(i)
    if len(set(f)) != len(f):
        continue
    l = len(f)
    c = (R//i)-((L-1)//i)
    tmp = c*(c-1)//2
    if l%2:
        ans+=tmp
    else:
        ans-=tmp
for i in range(max(2, L), R + 1):
    ans -= R // i - 1
ans *= 2

print(ans)