H,W = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(H)]

res = []
for i in range(H-1):
    for j in range(W):
        if a[i][j]%2 !=0:
            a[i+1][j]+=1
            res.append((i+1,j+1,i+2,j+1))
for i in range(W-1):
    if a[-1][i]%2 !=0:
        a[-1][i+1] += 1
        res.append((H,i+1,H,i+2))
print(len(res))
for a,b,c,d in res:
    print(a,b,c,d)