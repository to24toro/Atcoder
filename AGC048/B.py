from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)


n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ao = []
ae = []
bo = []
be = []
for i,a in enumerate(A):
    if i%2:
        ao.append([a,i])
    else:
        ae.append([a,i])

for i,b in enumerate(B):
    if i%2:
        bo.append([b,i])
    else:
        be.append([b,i])

ao.sort()
ae.sort()
bo.sort()
be.sort()
i = 0
ans = 0
n//=2
# print(ao,ae,bo,be)
set_ = set()
for _ in range(n):
    if not ao or not ae:
        x,i = bo.pop()
        y,j = be.pop()
        set_.add(i)
        set_.add(j)
        ans += x+y
        continue
    elif not bo or not be:
        x,i = ao.pop()
        y,j = ae.pop()
        set_.add(i)
        set_.add(j)
        ans += x+y
        continue
    elif ao[-1][0]+ae[-1][0]>bo[-1][0]+be[-1][0]:
        # print(ao[-1],ae[-1],ao,ae)
        x,i = ao.pop()
        y,j = ae.pop()
        set_.add(i)
        set_.add(j)
        ans += x+y
    else:
        x,i = bo.pop()
        y,j = be.pop()
        set_.add(i)
        set_.add(j)
        ans += x+y
    while ao and ao[-1][1] in set_:
        ao.pop()
    while ae and ae[-1][1] in set_:
        ae.pop()
    while bo and bo[-1][1] in set_:
        bo.pop()
    while be and be[-1][1] in set_:
        be.pop()
    
    

print(ans)
