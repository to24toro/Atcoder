from itertools import *
from collections import *
from heapq import *
import math
import sys
sys.setrecursionlimit(1<<20)
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1;b-=1
    g[a].append(b)
    g[b].append(a)
D = [0]*n
D[0]=1
def dfs(s,cur):
    for t in g[s]:
        if not D[t]:
            D[t]=cur+1
            dfs(t,cur+1)
    return
dfs(0,1)
# print(D)
p = D.index(max(D))
D = [0]*n
D[p]=1
dfs(p,1)
# p = D.index(max(D))
# D = [0]*n
# D[p]=1
# dfs(p,1)
print(*D)
while d:
    for i in g[s]:
        if dist[i]==d-1:
            x.append((s,i))
            y.add((s,i))
            s=i
            d-=1
            break
F = [deque() for _ in range(n)]
for i in range(n):
    for j in g[i]:
        if not (i,j) in y and not (j,i) in y:
            F[i].append(j)
now = 1
def dfs(s,now):
    st = []
    st.append(s)
    ans[s-1] = now
    while st:
        i = st[-1]
        f = 0
        while F[i]:
            j = F[i].popleft()
            if not ans[j-1]:
                f = 1
                ans[j-1]=now
                st.append(j)
                break
        if not f:
            st.pop()
            now +=1
    return now
