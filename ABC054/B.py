n,m = map(int,input().split())
A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(m)]
f = True
for i in range(0,n-m+1):
    for j in range(0,n-m+1):
        f = True
        for k in range(m):
            for l in range(m):
                if B[k][l]==A[i+k][j+l]:
                    continue
                else:
                    f = False
                    break
        if f:
            print('Yes');exit()
print('No')

