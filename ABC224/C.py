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
n= int(input())
L = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            xi,yi = L[i]
            xj,yj = L[j]
            xk,yk = L[k]
            xi-=xk
            xj-=xk
            yi-=yk
            yj-=yk
            if abs(xi*yj-xj*yi)>0:
                cnt+=1
print(cnt)
