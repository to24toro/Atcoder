from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')
n,k = map(int,input().split())
A = list(map(int,input().split()))
cnt=1
if k==1:
    L = [i for i in range(1,n+1)]
    print(*L[::-1]);exit()
else:
    P = [0]*(n+1)
    for a in A:
        P[a] += 1
    P[0] = 1
    idx = 1
    L = [A[0]]
    cnt=1
    for a in A[1:]:
        while idx<n and P[idx]==1:
            idx+=1
        p = idx
        print(p)
        if p<a:
            c=0
            while idx<n+1 and p<a and c<cnt:
                L.append(p)
                P[idx]+=1
                c+=1
                while idx<n and P[idx]==1:
                    idx+=1
                p = idx
            L.append(a)
            cnt=1
        else:
            L.append(a)
            cnt+=1
if cnt:
    for i in range(n+1):
        if P[i]==0:
            if cnt>1:
                L.append(i)
                cnt-=1
    for i in range(n,-1,-1):
        if P[i]==0:
            L.append(i)
print(L)