from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n = int(input())
A = list(map(int,input().split()))
P = []
N = []
if n==2:
    A.sort()
    print(A[1]-A[0])
    print(A[1],A[0]);exit()
for a in A:
    if a>=0:
        P.append(a)
    else:
        N.append(a)
P.sort()
N.sort(reverse=True)
if len(P)==0:
    print(-sum(N[1:])+N[0])
    print(N[0],N[1])
    s = N[0]-N[1]
    for i in range(n-2):
        print(s,N[i+2])
        s -=N[i+2]
    exit()
if len(N)==0:
    print(sum(P[1:])-P[0])
    print(P[0],P[1])
    s = P[0]-P[1]
    for i in range(n-3):
        print(s,P[i+2])
        s-=P[i+2]
    print(P[-1],s)
else:
    p = P[0]
    m = N[0]
    print(sum(P)-sum(N))
    for i in range(len(P)-1):
        print(m,P[i+1])
        m-=P[i+1]
    for i in range(len(N)-1):
        print(p,N[i+1])
        p-=N[i+1]
    print(p,m)

