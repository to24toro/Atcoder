<<<<<<< HEAD
=======
from decimal import Decimal
>>>>>>> c0748bd4c077c3dfd6e4d18e63f762403879af12
from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from array import *
import math
import sys
<<<<<<< HEAD
sys.setrecursionlimit(1<<20)
INF = float('inf')
=======
from decimal import *
sys.setrecursionlimit(1<<20)
INF = float('inf')

n = int(input())
L = []
for _ in range(n):
    x,y = map(int,input().split())
    a = x-1
    b = y
    c = x
    d = y-1
    e = Decimal(d)/Decimal(c)
    L.append([a,b,c,d,e])
L.sort(key = lambda x:[-x[4],-x[3]])
ans = 0
pd,pc = INF,1
for task in L:
    a,b,c,d,e = task
    if pd*a < pc*b:
        continue
    else:
        pd,pc = d,c
        ans +=1
print(ans)
>>>>>>> c0748bd4c077c3dfd6e4d18e63f762403879af12
