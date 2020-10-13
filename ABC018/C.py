r,c,k = map(int,input().split())
S = [list(map(int,input().replace('x','1').replace('o','0'))) for _ in range(r)]

L = []
for s in S:
    l = [0]*(c+1)
    for i,x in enumerate(s):
        l[i+1] = l[i]+ x
    L.append(l)

ans = 0

for i in range(k-1,c-k+1):
    for j in range(k-1,r-k+1):
        if all(L[j+p][i-abs(p)+k]-L[j+p][i+abs(p)-k+1]==0 for p in range(-k+1,k)):#辺のカウントだけで十分
            ans += 1
print(ans)