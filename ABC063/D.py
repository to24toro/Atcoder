from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n,a,b = map(int,input().split())
H = [int(input()) for _ in range(n)]
l,r = 0,10**10
c = a-b
while r-l>1:
    m = (r+l)//2
    x = m*b
    cnt = 0
    for i in range(n):
        y = H[i]-x
        if y<=0:continue
        cnt +=y//c
        if y%c:
            cnt += 1
    if m>=cnt:
        r = m
    else:
        l = m
print(r)