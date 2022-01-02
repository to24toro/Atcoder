from itertools import *
from collections import *
from heapq import *
from bisect import *
import math
import sys
sys.setrecursionlimit(1<<20)
n,x = map(int,input().split())

if x==1 or x==2*n-1:
    print('No');exit()
if n ==2:
    print('Yes')
    for i in range(1,4):
        print(i)
else:
    A = []
    print('Yes')
    if x==2:
        for i in range(5,2*n):
            A.append(i)
        for i in range(len(A)//2):
            print(A[i])
        print(3)
        print(2)
        print(1)
        print(4)
        for i in range(len(A)//2,len(A)):
            print(A[i])
    else:
        for i in range(1,x-2):
            A.append(i)
        for i in range(x+2,2*n):
            A.append(i)
        for i in range(len(A)//2):
            print(A[i])
        print(x-1)
        print(x)
        print(x+1)
        print(x-2)
        for i in range(len(A)//2,len(A)):
            print(A[i])