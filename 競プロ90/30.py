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
def get_sieve_of_eratosthenes_new(n):
    import math
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
L = get_sieve_of_eratosthenes_new(n)
ans =0
for i in range(2,n+1):
    cnt = set()
    s = 0
    I = i
    for l in L:
        while i%l==0:
            if l not in cnt:
                s += 1
                cnt.add(l)
            i//=l
    if s>=k:
        ans += 1
print(ans)