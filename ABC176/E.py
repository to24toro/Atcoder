from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
h,w,m = map(int,input().split())
H = [0]*(3*10**5+1)
W = [0]*(3*10**5+1)
L = []
for _ in range(m):
    a,b = map(int,input().split())
    H[a]+=1
    W[b]+=1
    L.append((a,b))
hx = max(H)
wx = max(W)
hh = H.count(max(H))
ww = W.count(max(W))
cnt = 0
for a,b in L:
    if H[a]==hx and W[b]==wx:
        cnt += 1
if cnt<hh*ww:
    print(hx+wx)
else:
    print(hx+wx-1)