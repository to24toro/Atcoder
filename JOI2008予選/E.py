r,c = map(int,input().split())
P = []
ans = 0
for _ in range(r):
    P.append(list(map(int,input().split())))
for bit in range(1<<r):
    Q = []
    for i in range(r):
        A = []
        if (bit>>i)&1:
            for j,p in enumerate(P[i]):
                A.append(1-p)
        else:
            for j,p in enumerate(P[i]):
                A.append(p)
        Q.append(A)
    cnt = 0
    for j in range(c):
        tmp = 0
        for i in range(r):
            tmp += Q[i][j]
        cnt += max(tmp,r-tmp)
    ans = max(ans,cnt)
print(ans)

