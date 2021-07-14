from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
II = 2**32-1
k,m = map(int,input().split())
m-=1
A = list(map(int,input().split()))
C = list(map(int,input().split()))
if m<k:
    print(A[m])
    exit()
def mat_mul(a,b):
    I,J,K = len(a),len(b[0]),len(b)
    c = [[0]*J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] ^= (a[i][k]&b[k][j])
    return c

def mat_pow(x,n):
    y = [[0]*len(x) for _ in range(len(x))]
    for i in range(len(x)):
        y[i][i] = II
    while n:
        if n&1:
            y = mat_mul(x,y)
        x = mat_mul(x,x)
        n>>=1
    return y

P = [C]
for i in range(k-1):
    tmp = [0]*k
    tmp[i]=II
    P.append(tmp)
# print(P)
PN = mat_pow(P,m-k+1)
C0 = PN[0]
# print(PN)
ans = 0
A = A[::-1]
for i in range(k):
    ans^=(C0[i]&A[i])
print(ans)