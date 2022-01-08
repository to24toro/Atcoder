from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
<<<<<<< HEAD
n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())
x = q-p+1
y = s-r+1
S = [["." for _ in range(y)] for _ in range(x)]
k = max(1-a,1-b)
l = min(n-a,n-b)
m = max(1-a,b-n)
t = min(n-a,b-1)
for i in range(max(0,a+k-p),min(x,a+l-p)+1):
    xx = p + i
    yy = xx+b-a
    if p<=xx<=q and r<=yy<=s:
        S[i][yy-r] = '#'
for i in range(max(0,a+m-p),min(x,a+t-p)+1):
    xx = p + i
    kk = xx-a
    yy = xx+b-a-2*kk
    if p<=xx<=q and r<=yy<=s:
        S[i][yy-r] = '#'
for s in S:
    print(''.join(s))
=======
>>>>>>> 7ef5272f22bc7d556fd1b34ce9cb0c92784a0a0b
