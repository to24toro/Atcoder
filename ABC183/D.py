from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,w = map(int,input().split())
A = [0]*(2*10**5+2)
for _ in range(n):
    s,t,p = map(int,input().split())
    A[s]+=p
    A[t]-=p
S = list(accumulate(A))
# print(S[:11])
print('Yes' if max(S)<=w else 'No')