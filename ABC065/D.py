n = int(input())
x,y = [],[]
for i in range(n):
    a,b = map(int,input().split())
    x.append([a,i])
    y.append([b,i])
x.sort()
y.sort()
g = [[] for _ in range(n)]
for i in range(n-1):
    g[x[i][1]].append([abs(x[i+1][0]-x[i][0]),x[i+1][1]])
    g[x[i+1][1]].append([abs(x[i+1][0]-x[i][0]),x[i][1]])
    g[y[i][1]].append([abs(y[i+1][0]-y[i][0]),y[i+1][1]])
    g[y[i+1][1]].append([abs(y[i+1][0]-y[i][0]),y[i][1]])
import heapq
hq = []
for d,e in g[0]:
    heapq.heappush(hq,[d,e])
cnt = 1
visit = [False]*n
visit[0] = True
ans = 0
while cnt <n:
    cost, end = heapq.heappop(hq)
    if visit[end]: continue
    ans += cost
    visit[end] = True
    cnt += 1
    for d,e in g[end]:
        if not visit[e]: #ここにifを入れて高速化させないと間に合わない
            heapq.heappush(hq,[d,e])
print(ans)
        
