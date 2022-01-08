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
B = [list(map(int,input().split())) for _ in range(n)]
prev = -1
for i in range(n):
    s = B[i][0]
    f =True
    if i!=0:
        if prev+7!=s:
            print('No');exit()
    if m!=1 and s%7==0:
        print('No');exit()
    prev = s
    for j in range(1,m):
        if s+1!=B[i][j]:
            f =False
            print('No');exit()
        elif j!=m-1 and (s+1)%7==0:
            print('No');exit()
        else:
            s +=1
print('Yes')