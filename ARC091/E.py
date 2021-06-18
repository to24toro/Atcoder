from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,a,b = map(int,input().split())
if a+b>n+1 or a*b<n:print(-1);exit()
A = []
s = n-a
cur = n
for _ in range(a):
    num = min(b-1,s)+1
    s-=num-1
    for j in range(num):
        A.append(cur-num+1+j)
    cur-=num
print(*A[::-1])