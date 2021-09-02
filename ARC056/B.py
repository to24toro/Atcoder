n,m,s = map(int,input().split())
s-=1
g = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    u-=1
    v-=1
    u,v = max(u,v),min(u,v)
    g[u].append(v)

seen = [0]*n
from heapq import *

hq = []
heappush(hq,s)
cur = 0;ans = set()
seen = [0]*n
chk = [0]*n
ans.add(s)
while hq:
    x = heappop(hq)
    for y in g[x]:
        if not seen[y]:
            seen[y] = 1
            # print(y)
            if cur<y:
                ans.add(y)
                chk[y] = 1
            if y==cur:
                chk[y]=1
                ans.add(y)
                for i in range(cur+1,n):
                    if chk[i]==0:
                        cur = i
                        break
                else:
                    break
            else:
                heappush(hq,y)
        if cur==s:
            ans.add(s)
            break
ans = sorted(list(ans))

for a in ans:
    print(a+1)

















# n,m,s = map(int,input().split())
# s-=1
# g = [[] for _ in range(n)]
# for _ in range(m):
#     u,v = map(int,input().split())
#     u-=1
#     v-=1
#     g[u].append(v)
#     g[v].append(u)
# import heapq
# hq = []
# hq = [(-float('inf'),s)]
# heapq.heapify(hq)
# seen = [0]*n
# vis = set()
# while hq:
#     c,p = heapq.heappop(hq)
#     if p in vis:continue
#     seen[p]=-c
#     vis.add(p)
#     for q in g[p]:
#         if q not in vis:
#             heapq.heappush(hq,(max(c,-p),q))
# for i in range(n):
#     if i<seen[i]:
#         print(i+1)