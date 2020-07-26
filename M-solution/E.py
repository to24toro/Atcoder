N = int(input())
X = []
Y = []
P = []
for _ in range(N):
    x,y,p = map(int,input().split())
    X.append(x)
    Y.append(y)
    P.append(p)
DX = [[0]*N for _ in range(1<<N)]
DY = [[0]*N for _ in range(1<<N)]

for i,x in enumerate(X):
    for k in range(1<<N):
        d = abs(x)
        for j,xx in enumerate(X):
            if k & (1<<j):
                d = min(d,abs(xx-x))
        DX[k][i] = d*P[i]
for i,y in enumerate(Y):
    for k in range(1<<N):
        d = abs(y)
        for j,yy in enumerate(Y):
            if k & (1<<j):
                d = min(d,abs(yy-y))
        DY[k][i] = d*P[i]

ANS = [1<<100]*(N+1)
PC = [0]*(1<<N)
for i in range(1,1<<N):
    PC[i] = PC[i^1] + 1 if i%2 else PC[i//2] 
RA = []
for i in range(1<<N):
    t = []
    for j in range(N):
        if i&(1<<j):
            t.append(j)
    RA.append(t)

mm = (1 << N) - 1
for i in range(1 << N):
    m = i ^ mm
    j = m
    dxi = DX[i]
    pci = PC[i]
    while 1:
        dyj = DY[j]
        ans = 0
        for k in RA[i^j^mm]:
            ans += min(dxi[k], dyj[k])
        
        pc = pci + PC[j]
        ANS[pc] = min(ANS[pc], ans)
        
        if not j:
            break
        j = m & (j - 1)
print(*ANS ,sep="\n")
