n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(m):
    for j in range(i,m):
        tmp = 0
        for k in range(n):
            tmp += max(A[k][i],A[k][j])
        ans = max(ans,tmp)
print(ans)