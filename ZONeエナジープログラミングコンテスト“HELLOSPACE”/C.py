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
L = [list(map(int,input().split())) for _ in range(n)]
ok,ng = 0,10**9+1
while ng-ok >1:
    mid = (ng+ok)//2
    A = set()
    for l in L:
        tmp = []
        for i in range(5):
            if l[i]>=mid:
                tmp.append("1")
            else:
                tmp.append("0")
        # print(tmp)
        A.add("".join(tmp))
    A = list(A)
    n = len(A)
    # print(A,ok,ng,mid)
    f =False
    if n==1:
        a = int(A[0],2)
        if a==31:
            f =True
    elif n==2:
        a,b = int(A[0],2),int(A[1],2)
        if a|b==31:
            f =True
    else:
        for i in range(n):
            a = A[i]
            a = int(a,2)
            for j in range(i+1,n):
                b = A[j]
                b = int(b,2)
                for k in range(j+1,n):
                    c = A[k]
                    c = int(c,2)
                    if a | b | c==31:
                        f =True
                        break
    if f:
        ok = mid
    else:
        ng = mid
print(ok)
