H,W,K = map(int,input().split())
cnt = 0
d = [[0]*(W) for _ in range(H)]
h = [0]*H
w = [0]*W
for i in range(H):
    A = input()
    for j in range(len(A)):
        if A[j]=='#':
            cnt += 1
            d[i][j] = 1
            h[i] += 1
            w[j] += 1
ans = 0
for i in range(2**H):
    I = bin(i)[2:]
    I = I.zfill(H)
    for j in range(2**W):
        J = bin(j)[2:]
        J = J.zfill(W)
        tmp = cnt
        for k in range(len(I)):
            if I[k]=='1':
                tmp-=h[k]
        for l in range(len(J)):
            if J[l] =='1':
                tmp-=w[l]
        for k in range(len(I)):
            for l in range(len(J)):
                if I[k]=='1' and J[l]=='1':
                    tmp += d[k][l]
        if tmp ==K:
            ans += 1
print(ans)

                



