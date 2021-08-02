from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,K = map(int,input().split())
S = list(map(lambda x: ord(x)-ord('a'),input()))
C = [[-1]*n for _ in range(26)]
for i in range(26):
    for j in range(n-1,-1,-1):
        if j<n-1:
            C[i][j] = C[i][j+1]
        if S[j]==i:
            C[i][j] = n-1-j
ans = []
j = 0
for k in range(K):
    for i in range(26):
        if K-k-1<=C[i][j]:
            ans.append(chr(i+ord('a')))
            j = n-C[i][j]
            break
print(*ans,sep = "")