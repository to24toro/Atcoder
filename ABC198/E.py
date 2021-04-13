n = int(input())
C = list(map(int,input().split()))
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
import sys
sys.setrecursionlimit(100000000)
from collections import deque
seen = [0]*n
dist = [float('inf')]*n
color = [0]*(10**5+1)
def dfs(s,d):
    for t in g[s]:
        f =True
        if dist[t]>dist[s]+1:
            dist[t]=dist[s]+1
            if color[C[t]]==0:
                # print(t,t,color[:11])
                ans.append(t)
                color[C[t]]+=1
                f =False
            dfs(t,d+1)
            if not f:
                color[C[t]]-=1
color[C[0]]=1
seen[0]=1
dist[0]= 0
ans = [0]
dfs(0,0)
# ans.sort()
# while q:
#     s,color,set_ = q.popleft()
#     set2 = copy(set_)
#     for t in g[s]:
#         if not seen[t]:
#             seen[t]=1
#             if C[t] not in set2:d
#                 ans.append(t)
#                 set2.add(C[t])
#             q.append((t,C[t],set2))
ans.sort()
for a in ans:
    print(a+1)