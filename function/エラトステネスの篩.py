from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7

n,k = map(int,input().split())
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
multi = MultipleFactorization(n)
print(multi.prime())
ans =0
for i in range(2,n+1):
    cnt = multi.count_prime(i)
    if cnt>=k:
        ans += 1

print(ans)