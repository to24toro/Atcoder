from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
P = list(map(lambda x:int(x)-1,input().split()))

for i in range(n):
    a = A[i]
    b = B[P[i]]
    if P[i]!=i and a<=b:
        print(-1);exit()

A = [[A[i],i] for i in range(n)]
A.sort(reverse=True)

ans = []
for i in range(n):
    t = A[i][1]
    while True:
        if P[t]==t:
            break
        ans.append([P[t]+1,t+1])
        tmp = P[P[t]]
        P[P[t]] = P[t]
        P[t] = tmp
print(len(ans))
for a in ans:
    print(*a)


    