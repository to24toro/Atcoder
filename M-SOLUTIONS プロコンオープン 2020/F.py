from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n = int(input())
U,D,L,R = [],[],[],[]
for _ in range(n):
    x,y,u = input().split()
    if u=='U': U.append((int(x),int(y)))
    if u=='R': R.append((int(x),int(y)))
    if u=='L': L.append((int(x),int(y)))
    if u=='D': D.append((int(x),int(y)))

ans = float('inf')

def solve(dd1,dd2,times):
    global ans
    for k,l1 in dd1.items():
        if not dd2[k]:continue
        l2 = dd2[k]
        l1.sort()
        l2.sort()
        pos = 0
        f = False
        for l in l2:
            while l1[pos]<l:
                pos+=1
                if pos ==len(l1):
                    f = True
                    break
            if f:
                break
            ans = min(ans,times*(l1[pos]-l))

dd_U = defaultdict(list)
dd_D = defaultdict(list)
for x,y in D:
    dd_D[x].append(y)
for x,y in U:
    dd_U[x].append(y)
solve(dd_D,dd_U,5)
dd_L = defaultdict(list)
dd_R = defaultdict(list)
for x,y in L:
    dd_L[y].append(x)
for x,y in R:
    dd_R[y].append(x)
solve(dd_L,dd_R,5)

dd_U = defaultdict(list)
dd_R = defaultdict(list)
for x,y in R:
    dd_R[x+y].append(x)
for x,y in U:
    dd_U[x+y].append(x)
solve(dd_U,dd_R,10)

dd_U = defaultdict(list)
dd_L = defaultdict(list)
for x,y in L:
    dd_R[x-y].append(x)
for x,y in U:
    dd_U[x-y].append(x)
solve(dd_L,dd_U,10)

dd_D = defaultdict(list)
dd_L = defaultdict(list)
for x,y in D:
    dd_D[x+y].append(x)
for x,y in L:
    dd_L[x+y].append(x)
solve(dd_L,dd_D,10)

dd_D = defaultdict(list)
dd_R = defaultdict(list)
for x,y in R:
    dd_R[x-y].append(x)
for x,y in D:
    dd_D[x-y].append(x)
solve(dd_D,dd_R,10)

print("SAFE" if ans == float("inf") else ans)