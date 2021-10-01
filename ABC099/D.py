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
n,c = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(c)]
C = [list(map(lambda x:int(x)-1,input().split())) for _ in range(n)]
A = [[0]*c for _ in range(3)]
for i in range(n):
    for j in range(n):
        A[(i+j)%3][C[i][j]]+=1
ans = INF

for i in range(c):
    for j in range(c):
        for k in range(c):
            if i==j or k==j or i==k:
                continue
            tmp = 0
            for l in range(c):
                tmp += D[l][i]*A[0][l] +D[l][j]*A[1][l]+D[l][k]*A[2][l]
                # print(i,j,k,l)
            ans = min(ans,tmp)
print(ans)