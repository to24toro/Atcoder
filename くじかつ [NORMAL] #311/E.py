n,c = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(c)]
C = [list(map(int,input().split())) for _ in range(n)]

x = [0]*c
y = [0]*c
z = [0]*c

for i in range(n):
    for j in range(n):
        if (i+j)%3==0:
            x[(C[i][j]-1)]+=1
        elif (i+j)%3==1:
            y[(C[i][j]-1)]+=1
        else:
            z[(C[i][j]-1)]+=1

ans = 0
res = float('inf')
for i in range(c):
    for j in range(c):
        for k in range(c):
            tmp = 0
            if i!=j and j!=k and i!=k:
                for l in range(c):
                    tmp += D[l][i]*x[l] + D[l][j]*y[l] + D[l][k]*z[l]
                # print(tmp)
                res = min(res,tmp)
print(res)