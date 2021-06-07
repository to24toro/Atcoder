from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
X = []
Y = []
for i in range(n):
    x,y = map(int,input().split())
    X.append([x,i])
    Y.append([y,i])
X.sort()
Y.sort()
# print(X,Y)
a = [abs(X[-1][0]-X[0][0]),X[-1][1],X[0][1]]
b = [abs(X[-2][0]-X[0][0]),X[-2][1],X[0][1]]
c = [abs(X[-1][0]-X[1][0]),X[-1][1],X[1][1]]
e = [abs(Y[-1][0]-Y[0][0]),Y[-1][1],Y[0][1]]
f = [abs(Y[-2][0]-Y[0][0]),Y[-2][1],Y[0][1]]
d = [abs(Y[-1][0]-Y[1][0]),Y[-1][1],Y[1][1]]
A = [a,b,c]
B = [d,e,f]
B.sort(reverse=True)
A.sort(reverse=True)
# print(A,B)
if A[0][1]!=B[0][1] or A[0][2]!=B[0][2]:
    C =[A[0][0],B[0][0],A[1][0],B[1][0]]
    C.sort()
    print(C[-2])
else:
    C =[max(A[0][0],B[0][0]),A[1][0],B[1][0]]
    C.sort()
    print(C[-2])

# print(A[1])
