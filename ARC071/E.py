from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

S = input()
T = input()
q = int(input())
ss = []
for s in S:
    if s=='A':
        ss.append(1)
    else:
        ss.append(2)
SS = [0]+list(accumulate(ss))
tt = []
for t in T:
    if t=='A':
        tt.append(1)
    else:
        tt.append(2)
TT = [0]+list(accumulate(tt))
# print(SS,TT)
for _ in range(q):
    a,b,c,d = map(int,input().split())
    a-=1
    c-=1
    s = SS[b]-SS[a]
    t = TT[d]-TT[c]
    if s%3==t%3:
        print('YES')
    else:
        print('NO')
