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
S = [sum(A)]
for a in A:
    S.append(S[-1]-a)
ans = 1
nodes = 1-A[0]
for i in range(1,n+1):
    ni = min(nodes*2,S[i])
    ans += ni
    nodes += nodes-A[i]
    if nodes<0:
        print(-1);exit()
if nodes<0:
    print(-1);exit()
print(ans)

