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
X = input()
M = int(input())
d = -INF
for x in X:
    d = max(d,int(x))

res = 0
X = [int(x) for x in X[::-1]]
l = len(X)
 
if l==1:
    if X[0]<=M:
        print(1)
    else:
        print(0)
    exit()
ok = d
ng = 10**18+1
while ng-ok>1:
    m = (ng+ok)//2
    res = 0
    for i,x in enumerate(X):
        res += pow(m,i)*x
        if res>M:
            res = INF
            break
    # print(res,m,ok,ng)
    if res<=M:
        ok = m
    else:
        ng = m
# print(ng,ok)
print(ok-d)
