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

n,P = map(int,input().split())
X = []
def f(L,R):
    if not L:
        z = P-R[-1]
        ans1 = len(R)*z
        for i,r in enumerate(R[:-1]):
            ans1 += R[-1]-r-1-i
        return ans1
    if not R:
        z = L[0]-1
        ans2 = len(L)*z
        for i,l in enumerate(L[1:]):
            ans2 += l-L[0]-i-1
        return ans2
    rr = 0
    ll = 0
    for i,r in enumerate(R[:-1]):
        rr += R[-1]-r-1-i
    for i,l in enumerate(L[1:]):
        ll += l-L[0]-1-i
    return max(ll + len(L)*(L[0]-R[-1]-1), rr + len(R)*(L[0]-R[-1])-1)
L = []
R = []
ans = 0
for i in range(n):
    c,d = input().split()
    c = int(c)
    if d=='L':
        L.append(c)
    else:
        if L:
            ans += f(L,R)
            L = []
            R = []
        R.append(c)

if R or L:
    ans += f(L,R)
print(ans)




n,l = map(int,input().split())
x = []
d = []
for i in range(n):
    a,b = input().split()
    x.append(int(a))
    d.append(b)
 
 
def f(L, R):
    if len(L)==0:
        z = l+1
    elif len(R)==0:
        z = 1
    elif len(L)>=len(R):
        z = R[-1]+1
    else:
        z = L[0]
    
    res = 0
    for i,x  in enumerate(R[::-1]):
        res+=z-1-i-x
    for i, x in enumerate(L):
        res+=x-(z+i)
    return res
 
L = []
R = []
ans = 0
for i in range(n):
    if d[i]=="L":
        L.append(x[i])
    else:
        R.append(x[i])
    if i==n-1:
        ans += f(L,R)
        L = []
        R = []
    elif d[i]=="L" and d[i+1]=="R":
        ans += f(L,R)
        L = []
        R = []
print(ans)