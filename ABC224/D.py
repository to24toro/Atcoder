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
<<<<<<< HEAD
=======
m = int(input())
s = set()
for _ in range(m):
    u,v = map(int,input().split())
    u-=1
    v-=1
    s.add((u,v))
    s.add((v,u))
L = [str(i) for i in range(9)]
D = defaultdict(list)
P = list(map(lambda x:str(int(x)-1),input().split()))
a = set([i for i in range(9)])
# for p in P:
#     a.remove(int(p))
Z = [str(8)]*9
for i,p in enumerate(P):
    Z[int(p)]=str(i)
# for i in range(9):
#     if i in a:
#         P+=str(i)
P = "".join(Z)
# print(P)
for v in permutations(L):
    l = list(v)
    ll = "".join(l)
    p = l.index('8')
    for i in range(9):
        if p!=i:
            if (i,p) in s or (p,i) in s:
                l[i],l[p] = l[p],l[i]
                lll = "".join(l)
                D[ll].append(lll)
                D[lll].append(ll)
                l[i],l[p] = l[p],l[i]

Q = '012345678'
q = deque([(P,0)])
# print(P,Q)
set_ = set()
set_.add(P)
while q:
    x,c = q.popleft()
    if x==Q:
        print(c);exit()
    for y in D[x]:
        if y not in set_:
            set_.add(y)
            q.append((y,c+1))
print(-1)
>>>>>>> c0748bd4c077c3dfd6e4d18e63f762403879af12
