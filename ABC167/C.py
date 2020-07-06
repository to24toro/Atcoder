N,M,X = map(int,input().split())
A = []
cost = []
for i in range(N):
    a = list(map(int,input().split()))
    A.append(a[1:])
    cost.append(a[0])
ans = float('inf')
for i in range(2**N):
    I = bin(i)[2:]
    I = I.zfill(N) #なんの数字で埋めるか気をつける
    tmp = [0]*M
    buy = 0
    for j in range(len(I)):
        if I[j]=='1':
            for k in range(len(A[j])):
                tmp[k] += A[j][k]
            buy += cost[j]
    if all(tmp[i]>=X for i in range(len(tmp))):
        ans = min(ans,buy)
ans = -1 if ans ==float('inf') else ans
print(ans)