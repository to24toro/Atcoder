from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
dx = [1,-1,0,0]
dy = [0,0,1,-1]
MOD = 10**9+7

n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i],y[i] = map(int,input().split())

# 偏角ソート
ans = 0
for i in range(n):
    ang = []
    for j in range(n):
        if i!=j:
            if x[i]==x[j]:
                if y[j]-y[i]>0:
                    ang.append(90)
                else:
                    ang.append(-90)
            else:
                ang.append(atan2(y[j]-y[i],x[j]-x[i])*180/pi)
    ang.sort()
    ang = [ang[-1]-360]+ang+[ang[0]+360]
    for j in range(1,n):
        tmp = ang[j] + 180
        if tmp>180:
            tmp-=360
        idx = bisect_left(ang,tmp)
        res = min(tmp-ang[idx-1],ang[idx]-tmp)
        ans = max(ans,180-res)
print(ans)
