from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)

S = list(input())
C = [0]*(len(S)+20)
ans = 0
def damage(a,c):
    return a*(1+c//10*0.1)
L = [0]*(len(S)+20)
start = 0
cur = 5
chk = 0
for i,s in enumerate(S):
    if i-5>=0 and L[i-5]==10:
        cur += 1
    if i-5>=0 and L[i-5]==50:
        cur += 3
    if chk>0:
        chk-=1
        continue
    if s =='-':
        continue
    elif s=='N':
        if cur>0:
            C[i] =10
            cur-=1
            L[i+2] = 10
        else:
            continue
    else:
        if cur>2:
            C[i] =50
            chk = 2
            cur-=3
            L[i+4] = 50
comb = 0
for i,(l,c) in enumerate(zip(L,C)):
    if c:
        ans += c*comb//10*0.1
        comb += 1
    if l>0:
        ans += l
print(L,ans)
    
            