w = int(input())
n,K = map(int,input().split())
A = []
B = []
for _ in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
dp = [[[0]*(w+2) for _ in range(K+2)] for _ in range(n+2)]#dp[i][j][k]:k枚目まで調べた時幅iで使用数jの時の最大値

for k in range(w+1):
    for j in range(K+1):
        for i in range(n):
            if k+A[i] <= w:
                dp[i+1][j+1][k+A[i]] = max(dp[i][j][k]+B[i], dp[i][j][k+A[i]])
        
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
print(dp[n][K][w])