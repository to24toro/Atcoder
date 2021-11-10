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

y = int(input())
for _ in range(y):
    r,g,b = map(int,input().split())
    A = [r,g,b]
    A.sort()
    r,g,b = A
    f =False
    res = INF
    if (b-g)%3==0:
        cnt = (b-g)//3
        ans = b
        res = min(res,ans)
        f =True
    if (g-r)%3==0:
        cnt = (g-r)//3
        ans1 =g
        res = min(res,ans1)
        f = True
    if (b-r)%3==0:
        cnt = (b-r)//3
        ans4 = b
        res = min(res,ans4)
        f=True
    if r ==g:
        ans2 = r
        res = min(res,ans2)
        f=True
    if g==b:
        ans3=g
        res = min(res,ans3)
        f =True
    if f:
        print(res)
    else:
        print(-1)
    

    