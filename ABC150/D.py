from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m = map(int,input().split())

A = list(map(int,input().split()))

A = [a//2 for a in A]
B = []
for a in A:
    cnt = 0
    while a%2==0:
        a//=2
        cnt += 1
    B.append(cnt)
l  = len(set(B))
if l>1:
    print(0);exit()
g = A[0]
s = A[0]
for a in A:
    g = math.gcd(s,a)
    s = s*a//g
cnt = m//s
if cnt%2:
    print(cnt//2+1)
else:
    print(cnt//2)