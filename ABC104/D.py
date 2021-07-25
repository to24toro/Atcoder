from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

MOD = 10**9+7
S = input()
A = []
B = []
C = []
D = []
for i,s in enumerate(S):
    if s == 'A':
        A.append(i)
    elif s == 'B':
        B.append(i)
    elif s == 'C':
        C.append(i)
    else:
        D.append(i)
ans = 0

if len(D)>0:
    x = pow(3,len(D)-1,MOD)
else:
    x = 0
if len(D)>1:
    y = pow(3,len(D)-2,MOD)
else:
    y = 0
if len(D)>2:
    z = pow(3,len(D)-3,MOD)
else:
    z = 0

for b in B:
    a = bisect_left(A,b)
    c = len(C)-bisect_left(C,b)
    da = bisect_left(D,b)
    dc = len(D)-bisect_left(D,b)
    ans += a*c*pow(3,len(D),MOD)
    ans %=MOD
    ans += da*dc*y
    ans %=MOD
    ans += da*c*x
    ans %=MOD
    ans += a*dc*x
    ans %=MOD
for i,d in enumerate(D):
    a = bisect_left(A,d)
    c = len(C)-bisect_left(C,d)
    da = i
    dc = len(D)-i-1
    ans += a*c*x
    ans %=MOD
    if da>0 and dc>0:
        ans += da*dc*z
        ans %=MOD
    if da>0:
        ans += da*c*y
        ans %=MOD
    if dc>0:
        ans += a*dc*y
        ans %=MOD
print(ans)