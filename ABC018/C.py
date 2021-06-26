from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
R,C,K = map(int,input().split())
S = [input() for _ in range(R)]
L = []
for i in range(R):
    tmp = []
    for j in range(C):
        if S[i][j]=='o':
            tmp.append(True)
        else:
            tmp.append(False)
    L.append(tmp)
# print(L)
for _ in range(K-1):
    LL = [[False]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if 1<=i<R-1 and 1<=j<C-1:
                LL[i][j] = LL[i][j] and L[i-1][j] and L[i+1][j] and L[i][j-1] and L[i][j+1]
    L = LL
    print(L)
ans = 0
for i in range(R):
    for j in range(C):
        if L[i][j]:
            ans += 1
print(ans)