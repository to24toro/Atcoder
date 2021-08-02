from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
<<<<<<< HEAD
INF = float('inf')
=======
INF = float('inf')

n,K = map(int,input().split())
s = set()
A = [[0]*K for i in range(n)]
for i in range(K):
    c,k = map(str,input().split())
    k = int(k)
    if c =='L':
        for j in range(k,n):
            A[j][i] += 1
    else:
        for j in range(k-1):
            A[j][i] += 1
    s.add(k-1)
if len(s)!=K:
    print(0)
else:
    MOD = 998244353
    ans = 1
    for i in range(n):
        if i in s:
            continue
        ans *= sum(A[i])
        ans%=MOD
    print(ans)

>>>>>>> d3b13ade2f4f0f628896542768ac5119b659c4e1
