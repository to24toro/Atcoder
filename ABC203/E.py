from itertools import *
from collections import *
from heapq import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)

n,m = map(int,input().split())
ans = set()
ans.add(n)
dic = defaultdict(list)
for _ in range(m):
    x,y = map(int,input().split())
    dic[x].append(y)
L = sorted(dic.items())
# print(L)
for k,li in L:
    set_ = set()
    for l in li:
        if l-1 in ans:
            set_.add(l)
        if l+1 in ans:
            set_.add(l)
    for l in li:
        if l in ans:
            ans.remove(l)
    ans |= set_
print(len(ans))
        
# g = defaultdict(list)
# dic = defaultdict(int)
# seen = defaultdict(int)
# L = [(0,n)]
# set_ = set()
# for _ in range(m):
#     x,y = map(int,input().split())
#     dic[y] = max(dic[y],x)
#     L.append((x,y))
#     set_.add((x,y))
# for x,y in L:
#     if (x+1,y+1) in set_:
#         g[(x,y)].append((x+1,y+1))
#     if (x+1,y-1) in set_:
#         g[(x,y)].append((x+1,y-1))

# ans = 1 if dic[y]==0 else 0

# q = deque([(0,n)])
# while q:
#     x,y = q.popleft()
#     for x1,y1 in g[(x,y)]:
#         if not seen[(x1,y1)]:
#             seen[(x1,y1)]=1
#             q.append((x1,y1))
# ds = {}
# for k,v in dic.items():
#     if seen[(v,k)]:
#         ans += 1
#         ds[k]=1
# for x,y in L:
#     j = 0
#     if x==2*n and y not in ds:
#         if seen[(x-1,y-1)]==1:
#             j =1
#         else:
#             if y-1 in ds:
#                 j = 1
#         if seen[(x-1,y+1)]==1:
#             j =1
#         else:
#             if y+1 in ds:
#                 j = 1
#     ans += j
        
# print(ans)
    
