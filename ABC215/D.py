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
A = list(map(int,input().split()))
ma = max(A)
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
multi = MultipleFactorization(max(ma,m))
primelist = multi.prime()
primelist.sort()
ans = [1]
set_ = set()
for a in A:
    al = multi.factorization(a)
    for aa in al:
        set_.add(aa)
for x in range(2,m+1):
    y = x
    factors = []
    f=True
    while x > 1:
        k = multi.data[x]
        if k not in set_:
            factors.append(k)
            x //= k
        else:
            f =False
            break
    if f:
        ans.append(y)
print(len(ans))
for a in ans:
    print(a)
    


