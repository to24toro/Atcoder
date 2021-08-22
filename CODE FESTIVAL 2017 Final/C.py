n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
def nibu(n,g):
    from collections import deque
    q = deque([(0,0)])
    color = [-1]*n
    color[0] = 0
    while q:
        x,c = q.popleft()
        for y in g[x]:
            if color[y]==c:
                return False,[]
            if color[y]==-1:
                color[y]=1-c
                q.append((y,1-c))
    return True,color

flag,color = nibu(n,g)
# print(color)
if flag:
    s = sum(color)
    print(s*(n-s)-m)
else:
    print(n*(n-1)//2-m)
