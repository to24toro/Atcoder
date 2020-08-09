n,m = map(int,input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

ans = 0
for i in range(1<<n):
    cnt = 0
    flag = True
    L = []
    for j in range(n):
        if (i>>j)&1:
             L.append(j)
    for j in range(len(L)-1):
        if not flag: break
        for k in range(j+1,len(L)):
            if L[j] not in g[L[k]]:
                flag = False
                break
    if flag:
        ans = max(ans,len(L))
print(ans)