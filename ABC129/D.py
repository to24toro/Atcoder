h,w = map(int,input().split())
S = []
for _ in range(h):
    s = input()
    S.append(s)
L = []
R = []
for i in range(h):
    l = [0]
    for j in range(w):
        if S[i][j]=='#':
            l.append(0)
        else:
            l.append(l[-1]+1)
    L.append(l[1:])
    r = [0]
    for k in range(w-1,-1,-1):
        if S[i][k]=='#':
            r.append(0)
        else:
            r.append(r[-1]+1)
    R.append(r[1:][::-1])
U = []
D = []
for j in range(w):
    u = [0]
    for i in range(h):
        if S[i][j]=='#':
            u.append(0)
        else:
            u.append(u[-1]+1)
    U.append(u[1:])
    d = [0]
    for k in range(h-1,-1,-1):
        if S[k][j]=='#':
            d.append(0)
        else:
            d.append(d[-1]+1)
    D.append(d[1:][::-1])
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans,U[j][i]+D[j][i]+R[i][j]+L[i][j]-3)
print(ans)



