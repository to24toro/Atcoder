from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
set_ = set()
n,k = map(int,input().split())
p = (n-2)*(n-1)//2
if k>p:
    print(-1);exit()

print(n-1+p-k)
for i in range(2,n+1):
    print(1,i)

s = 2
p-=k

while p>0:
    for t in range(s+1,n+1):
        print(s,t)
        p-=1
        if p==0:
            break
    s += 1

