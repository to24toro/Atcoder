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
S = sum(A)
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
L = make_divisors(S)
ans = 1
L.sort()
for l in L[1:]:
    D = []
    for a in A:
        D.append(a%l)
    D.sort()
    cnt = 0
    P = []
    M = []
    for d in D:
        M.append(-d)
        P.append(l-d)
    PP = [0]+list(accumulate(P))
    MM = [0]+list(accumulate(M))
    for i in range(n):
        cnt = MM[i] + PP[-1]-PP[i]
        if -MM[i]<=k and cnt==0:
            ans = max(ans,l)
    # print(P,M,l,cnt)
print(ans)