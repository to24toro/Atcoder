from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
A = list(map(int,input().split()))

S = list(accumulate(A))
T = list(accumulate(S))
mx = 0
print(S)
for i in range(n):
    mx = max(A[i],mx)
    if i==0:
        print(S[i]+mx)
    else:
        print(S[i]+mx*(i+1)+T[i-1])
