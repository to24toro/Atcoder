from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
X,Y,A,B,C = map(int,input().split())
if A+B+C>X*Y:print('No');exit()
def helper(X,Y,A,B,C):
    def h(p,q,B,C):
        if q<0:return False
        if B+C>p*q:
            return False
        b = (B+p-1)//p
        c = (C+p-1)//p
        if b+c<=q:return True
        return False
    a = (A+X-1)//X
    if a<=Y and (h(X,Y-a,B,C) or h(Y-a,X,B,C)):
        return True
    else:
        return False
S = [A,B,C]
for xx in permutations(range(3)):
    xxx = list(xx)
    p,q,r = S[xxx[0]],S[xxx[1]],S[xxx[2]]
    res = helper(X,Y,p,q,r)
    res1 = helper(Y,X,p,q,r)
    if res or res1:
        print('Yes');exit()
print('No')

