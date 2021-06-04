from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,k = map(int,input().split())
S = input()
T = S[n-k:]
j = 0
ans = []
for i in range(n):
    s = S[i]
    t = T[j]
    if s<=t:
        ans.append(s)
        j += 1
    if j>=k:
        break
print(''.join(ans))