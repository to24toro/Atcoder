n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
g = []
p = [-1]*n
g = [[] for _ in range(n)]

for _ in range(m):
    c,d = map(int,input().split())
    g[c-1].append(d-1)
    g[d-1].append(c-1)
seen = [False]*n
from collections import deque
for i in range(n):
    if p[i]<0:
        p[i]=i
        q = deque([(i,i)])
        while q:
            u,d = q.popleft()
            for v in g[u]:
                if p[v]<0:
                    p[v]=d
                    q.append((v,d))

da = [0]*(n)
db = [0]*(n)
for i in range(n):
    # print(p[i],i,A[i],B[i])
    da[p[i]]+=A[i]
    db[p[i]]+=B[i]
for i in range(n):
    if da[i]==db[i]:
        continue
    else:
        print('No');exit()
print('Yes')
