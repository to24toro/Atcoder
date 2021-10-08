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
n,m,k = map(int,input().split())
A = list(map(int,input().split()))
MOD = 10**9+7
B = [[0]*n for _ in range(n)]
g = [[] for _ in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    x-=1;y-=1
    g[x].append(y)
    g[y].append(x)
m1 = pow(2*m,MOD-2,MOD)
for i in range(n):
    t = len(g[i])
    B[i][i] = (1-t*m1)%MOD
for i in range(n):
    for j in g[i]:
        if i!=j:
            B[i][j] = m1

def mat_mul(a,b):
    I,J,K = len(a),len(b[0]),len(b)
    c = [[0]*J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k]*b[k][j]
                c[i][j] %= MOD
    return c

def mat_pow(x,n):
    y = [[0]*len(x) for _ in range(len(x))]
    for i in range(len(x)):
        y[i][i] = 1
    while n:
        if n&1:
            y = mat_mul(x,y)
        x = mat_mul(x,x)
        n>>=1
    return y
AA = mat_pow(B,k)
ANS = [0]*n
for i in range(n):
    for j in range(n):
        ANS[i]+=AA[i][j]*A[j]
        ANS[i]%=MOD
print(*ANS,sep="\n")
