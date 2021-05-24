from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

mod = 998244353

h,w = map(int,input().split())
S = [input() for _ in range(h)]
D = [[0,0,0] for _ in range(h+w-1)]
n = h+w-2
ans = 1
for i in range(h):
    for j in range(w):
        if S[i][j]=='B':
            D[i+j][0]+=1
        elif S[i][j]=='R':
            D[i+j][1]+=1
        else:
            D[i+j][2] += 1
for i in range(n+1):
    b,r,x = D[i]
    if b==0 and r ==0:
        ans *= 2
        ans %=mod
    elif b==0 or r==0:
        continue
    else:
        print(0);exit()

print(ans%mod)