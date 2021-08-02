from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
import numpy as np
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7
def dp(i,j,val):
    return [[val]*j for _ in range(i)]

n,l = map(int,input().split())
k = int(input())
A =list(map(int,input().split()))
ok,ng = 0,l
while ng-ok>1:
    m = (ok+ng)//2
    cnt = 0
    tmp = 0
    for a in A:
        if a -tmp >=m:
            cnt += 1
            tmp = a
        else:
            continue
    if l-tmp >=m:
        cnt += 1
    if cnt >=k+1:
        ok = m
    else:
        ng = m
print(ok)