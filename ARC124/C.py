from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
import sys
import random
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]

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
X = make_divisors(A[0][0])
Y = make_divisors(A[0][1])
ans = -INF

for x in X:
    for y in Y:
        f =True
        for i in range(1,n):
            a,b = A[i]
            if (a%x==0 and b%y==0) or (a%y==0 and b%x==0):
                continue
            else:
                f =False
                break
        if f:
            ans = max(ans,x*y//gcd(x,y))
print(ans)


