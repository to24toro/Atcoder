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
n = int(input())
s = input()
S = [-1]*(3*n)
D = ["ABC","ACB","BAC","BCA","CAB","CBA"]
p = 1
for i,d in enumerate(D):
    L = list(d)
    m = 0
    t = 0
    f=False
    a,b,c, = -1,-1,-1
    while m<3*n:
        if L[t]==s[m] and S[m]==-1:
            if t==2:
                c = m
                S[a] = str(p)
                S[b] = str(p)
                S[c] = str(p)
                a,b,c = -1,-1,-1
                f=True
                t = 0
            elif t==1:
                t = 2
                b = m
            else:
                t = 1
                a = m
            m+=1
        else:
            m +=1
    if f:
        p += 1
print("".join(S))




    
