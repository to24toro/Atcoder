from itertools import *
from collections import *
from heapq import *
import math

n,c = map(int,input().split())
L = [tuple(map(int,input().split())) for _ in range(n)]
ans = -float('inf')
r0=[0]*(n+1)
r1=[0]*(n+1)
s = 0
for i in range(n):
    x,v = L[i]
    s += v
    r0[i+1] = max(r0[i],s-x)
    r1[i+1] = max(r1[i],s-2*x)
l0=[0]*(n+1)
l1=[0]*(n+1)
s = 0
for i in range(n-1,-1,-1):
    x,v = L[i]
    s += v
    l0[i] = max(l0[i+1],s-(c-x))
    l1[i] = max(l1[i+1],s-2*(c-x))
for i in range(n+1):
    ans = max(ans,l0[i]+r1[i],r0[i]+l1[i])
print(ans)


