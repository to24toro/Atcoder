from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,k = map(int,input().split())
d=dict()
MOD=10**9+7
i=1
while i<=n:
  x=n//i
  y=n//x+1
  d[x]=y-i
  i=y
P=len(d)
D=list(d.values())
A=[0 for _ in range(P)]
A[0]=1
for _ in range(k):
    b=0
    B=[0 for _ in range(P)]
    for i in range(P):
        b+=A[i]
        B[-i-1]=b*D[-i-1]%MOD
    A=B.copy()
print(sum(B)%MOD)
