from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m = map(int,input().split())

A = list(map(int,input().split()))
ans = 0
B = set()
for a in A:
    cnt = 0
    while a%2==0:
        a//=2
        cnt += 1
    B.add(cnt)
if len(B)!=1:
    print(0);exit()
A = [a//2 for a in A]
s = A[0]
for a in A[1:]:
    s*=a//math.gcd(s,a)
x = m//s
print((x+1)//2)
