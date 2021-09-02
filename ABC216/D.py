from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')


n,m = map(int,input().split())
L = []
for i in range(m):
    k = int(input())
    l = list(map(int,input().split()))
    L.append(l[::-1])

cnt = 2*n
s = [-1]*(n+1)
P = list(range(m))

while cnt>0:
    nP = []
    pre = cnt
    for i in P:
        if L[i]:
            l = L[i]
            if s[l[-1]]!=-1:
                cnt-=2
                nP.append(i)
                nP.append(s[l[-1]])
                L[s[l[-1]]].pop()
                l.pop()
            else:
                s[l[-1]]=i
    nP.sort()
    if pre ==cnt:
        print('No');exit()
    P = nP
print('Yes')

