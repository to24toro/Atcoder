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
mod = 10**9+7
if n==k:
    ans = 1
    for a in A:
        ans = (ans*a)%mod
    print(ans);exit()
if k%2:
    f = True
    for a in A:
        if a>0:
            f = False
    if f:
        ans = 1
        A.sort(reverse=True)
        for a in A[:k]:
            ans = (ans*a)%mod
        print(ans);exit()
AA = []
for a in A:
    if a<0:
        AA.append([-a,1])
    else:
        AA.append([a,0])
AA.sort(reverse=True)
b = 0
for a,i in AA[:k]:
    b += i
if b%2==0:
    ans = 1
    for a,_ in AA[:k]:
        ans = (ans*a)%mod
    print(ans)
else:
    AAA = AA[:k][::-1]
    p,m = INF,INF
    for a,i in AAA:
        if i==0 and p==INF:
            p = a
        if i==1 and m==INF:
            m = a
        if p!=INF and m!=INF:
            break
    AAA = AA[k:]
    pp,mm = INF,INF
    for a,i in AAA:
        if i==0 and pp==INF:
            pp = a
        if i==1 and mm==INF:
            mm = a
        if pp!=INF and mm!=INF:
            break
    if mm==INF:
        s = m
        t = pp
    elif pp==INF:
        s = p
        t = mm
    else:
        if abs(p*pp)>=abs(m*mm):
            s = m
            t = pp
        else:
            s = p
            t = mm
    ans = 1
    f = False
    for a,i in AA[:k]:
        if a==s and not f:
            f = True
        else:
            ans = (ans*a)%mod
    ans = (ans*t)%mod
    print(ans)
    


