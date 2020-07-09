n,m,q = map(int,input().split())
l = []
def dfs(a):
    if len(a)==n: l.append(a)
    else:
        for i in range(a[-1],m+1):
            dfs(a+[i])
for i in range(m):
    dfs([i+1])
Query = [list(map(int,input().split())) for _ in range(q)]
ans = 0
for li in l:
    tmp = 0
    for a,b,c,d in Query:
        if li[b-1]-li[a-1]==c:
            tmp += d
    ans = max(ans,tmp)
print(ans)