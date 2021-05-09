n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b,l = map(int,input().split())
    a-=1
    b-=1
    g[a].append(l)
    g[b].append(l)
ans = 0
for i in range(n):
    D = [0]*2541
    for l in g[i]:
        D[l]+=1
    for j in range(1000,1271):
        if j==1270:
            ans +=D[j]*(D[j]-1)//2
        else:
            ans += D[j]*D[2540-j]
print(ans)