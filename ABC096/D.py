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
class  MultipleFactorization:
    def __init__(self,n):
        self.data = [i for i in range(n+1)]
        self.n = n
        self._get_sieve()
    def _get_sieve(self):
        import math
        for i in range(2,int(math.sqrt(self.n))+1):
            if self.data[i]!=i:
                continue
            j = i
            while j <=self.n:
                if self.data[j]==j:
                    self.data[j] = i
                j +=i
    def prime(self):
        res = []
        for i in range(2,self.n+1):
            if self.data[i]==i:
                res.append(i)
        return res
    def factorization(self,x):
        factors = []
        while x > 1:
            k = self.data[x]
            factors.append(k)
            x //= k
        return factors
    def count_prime(self,x):
        cnt = 0
        s = set()
        while x>1:
            k = self.data[x]
            if k not in s:
                cnt += 1
                s.add(k)
            x//=k
        return cnt
n = 55556
multi = MultipleFactorization(n)
L = multi.prime()
A = []
n = int(input())
for l in L:
    if l%5==1:
        A.append(l)
print(*A[:n])
