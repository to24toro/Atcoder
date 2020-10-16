n,m,s,t = map(int,input().split())
s-=1
t-=1
y = [[] for _ in range(n)]
su = [[] for _ in range(n)]
for _ in range(m):
    u,v,a,b = map(int,input().split())
    u -=1
    v -=1
    y[u].append((v,a))
    y[v].append((u,a))
    su[u].append((v,b))
    su[v].append((u,b))
from collections import deque
si = [float('inf')]*n
ti = [float('inf')]*n
def bfs(s,li,mon):
    q = deque([(s,0)])
    li[s] = 0
    while q:
        u,cost = q.popleft()
        for v,change in mon[u]:
            if li[v] > change +cost:
                li[v] = change + cost
                q.append((v,li[v]))
    return
bfs(s,si,y)
bfs(t,ti,su)
cost = []
for i in range(n):
    cost.append((i,si[i]+ti[i]))
cost.sort(key = lambda x:x[1])
idx = 0
for i in range(n):
    if i<=cost[idx][0]:
        print(10**15-cost[idx][1])
    else:
        while idx<n:
            idx +=1
            if i<=cost[idx][0]:
                print(10**15-cost[idx][1])
                break
