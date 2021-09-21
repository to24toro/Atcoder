from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
S = input()
k = int(input())
l=10
SS = S*l
set_ = set()
n = len(S)
x,y = 0,0
set_.add((x,y))
pre = 0
dif = -INF
cnt = 0
ans = 0
ss = set()
while True:
    for i in range(n):
        if S[i]=='R':
            x+=1
        elif S[i]=='L':
            x-=1
        elif S[i]=='U':
            y += 1
        else:
            y-=1
        set_.add((x,y))
    cnt += 1
    nx = len(set_)
    ndif = nx-pre
    if ndif in ss:
        break
    ss.add(ndif)
    dif = ndif
    pre = nx
    ans =nx
print(ans+(k-cnt+1)*dif)