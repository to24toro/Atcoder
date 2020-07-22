n,m = map(int,input().split())
g =[[] for _ in range(n)]
for _ in range(m):
    x,y = map(int,input().split())
    x -=1
    y -=1
    g[x].append(y)
longest = [-1]*n
def dfs(i):
    if longest[i]==-1:
        l = -1
        for nx in g[i]:
            l = max(l,dfs(nx))
        if l ==-1:
            longest[i]=0
        else:
            longest[i] = 1+l
    return longest[i]
for i in range(n):
    if longest[i]==-1:
        dfs(i)
print(max(longest))
