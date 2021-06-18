from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,q = map(int,input().split())
A =[0]+ list(map(int,input().split()))
AA = []
for i in range(n):
    AA.append(A[i+1]-A[i]-1)
S = list(accumulate(AA))
for _ in range(q):
    k = int(input())
    idx = bisect_left(S,k)
    if idx==n:
        print(A[-1]+k-S[-1])
    elif idx==0:
        print(k)
    else:
        s = k-S[idx-1]
        print(A[idx]+s)