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

n,m = map(int,input().split())
X = [0]*(2*n)
Y = [i for i in range(2*n)]
A = [list(input()) for _ in range(2*n)]

for i in range(m):
    for j in range(n):
        a,b = Y[2*j],Y[2*j+1]
        aa,bb = A[a][i],A[b][i]
        if aa=='G' and bb=='P':
            X[b]+=1
        elif aa=='P' and bb=='C':
            X[b]+=1
        elif aa=='C' and bb=='G':
            X[b]+=1
        elif aa=='G' and bb=='C':
            X[a]+=1
        elif aa=='P' and bb=='G':
            X[a]+=1
        elif aa=='C' and bb=='P':
            X[a]+=1
    Y = []
    for i,x in enumerate(X):
        Y.append([x,i])
    Y.sort(key = lambda x:(-x[0],x[1]))
    Z = []
    for i,y in Y:
        Z.append(y)
    Y = Z
ANS = []
for i,x in enumerate(X):
    ANS.append((x,i))

ANS.sort(key = lambda x:(-x[0],x[1]))
for a,i in ANS:
    print(i+1)

