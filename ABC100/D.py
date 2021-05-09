n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for bit in range(1<<3):
    X = [-1]*3
    for i in range(3):
        if (bit>>i)&1:
            X[i]=1
    L.sort(key=lambda x:[x[0]*X[0]+x[1]*X[1]+x[2]*X[2]])
    x,y,z = 0,0,0
    for a,b,c in L[:m]:
        x+=a
        y+=b
        z+=c

    ans = max(ans,abs(x)+abs(y)+abs(z))
print(ans)
