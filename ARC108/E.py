from collections import deque


n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u,v,c = map(int,input().split())
    u-=1;v-=1;c-=1
    g[u].append((v,c))
    g[v].append((u,c))
ans = [-1]*n

q = deque([(0,0)])
ans[0] = 0
while q:
    c,x = q.popleft()
    for y,nc in g[x]:
        if ans[y]==-1:
            if ans[x]==c:
                ans[y] = (ans[x]+1)%n
            else:
                ans[y] = c
            print(x,y,ans)
            q.append((nc,y))
for i in range(n):
    print(ans[i]+1)
