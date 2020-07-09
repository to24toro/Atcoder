n,m,s = map(int,input().split())
import collections
g = [[] for _ in range(n+1)]
dic = {}
for _ in range(m):
    u,v,a,b = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
    dic[(u,v)]=(a,b)
    dic[(v,u)]=(a,b)
arr = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]
cost =[[float('inf')]*2501 for _ in range(n+1)]
for i in range(min(2500,s)+1):
    cost[1][i] = 0
q=collections.deque()
q.append(1)
while q:
    v = q.popleft()
    c,d = arr[v]
    for i in range(c,2501):
        cost[v][i] = min(cost[v][i],cost[v][i-c]+d)
    for u in g[v]:
        a,b = dic[(v,u)]
        flag = False
        for i in range(a,2501):
            if cost[u][i-a]>cost[v][i]+b:
                cost[u][i-a]=cost[v][i]+b
                flag = True
        if flag==True:
            q.append(u)
for i in range(2,n+1):
    print(min(cost[i]))