from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,k = map(int,input().split())
A = list(map(int,input().split()))
idx = 0

while idx<k:
    l = [0]*(n+1)
    for i,a in enumerate(A):
        mn = max(0,i-a)
        mx = min(n,i+a+1)
        l[mn]+=1
        l[mx]-=1
    S = list(accumulate(l))
    # print(S)
    idx+=1
    A = S
    if S[:-1].count(n)>=n:
        print(*S[:-1]);exit()
print(*S[:-1])

