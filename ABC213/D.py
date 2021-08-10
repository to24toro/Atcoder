from itertools import *
from collections import *
from heapq import *
from bisect import *
from copy import *
import math
import sys
sys.setrecursionlimit(1<<20)
INF = float('inf')

n = int(input())
gg = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    heappush(gg[a],b)
    heappush(gg[b],a)

g = [[] for _ in range(n)]
for i in range(n):
    while gg[i]:
        x = heappop(gg[i])
        g[i].append(x)
s = [INF]*n
ans = []
L = [[INF,INF] for _ in range(n)]
# def dfs(i,cnt):
#     L[i][0] = cnt
#     for j in g[i]:
#         if i!=j:
#             cnt = dfs(j,cnt+1)
#     cnt += 1
#     print(L)
#     L[i][1] = cnt
#     return cnt
# dfs(0,1)
# dic = {}
# for i in range(n):
#     a,b = L[i]
#     dic[a] = i + 1
#     dic[b] = i + 1
def dfs(i,pre,cnt):
    if L[i][0]==INF:
        L[i][0] = cnt
    f =True
    for j in g[i]:
        f = False
        if not ans:
            ans.append(i+1)
        elif ans[-1] !=i+1:
            ans.append(i+1)
        if L[j][0] == INF:
            dfs(j,i,cnt+1)
    cnt += 1
    L[i][1] = cnt
    if ans[-1] !=i+1:
        ans.append(i+1)
dfs(0,-1,1)
# for i in range(2*n):
#     if dic[i]:
#         ans.append(dic[i])
print(*ans)
