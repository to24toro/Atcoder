h,w = map(int,input().split())
A = []
for _ in range(h):
    a = list(map(int,input().split()))
    A.append(a)
B = []
for _ in range(h):
    b = list(map(int,input().split()))
    B.append(b)
g = [[0]*(w+1) for _ in range(h+1)]
m = 0
for i in range(1,h+1):
    for j in range(1,w+1):
        g[i][j] = abs(A[i-1][j-1]-B[i-1][j-1])
m  = 80*(h+w-1)//2
dp = [[[False for _ in range(m+1)] for _ in range(w+1)] for _ in range(h+1)]
dp[1][1][g[1][1]] = True

for i in range(1,h+1):
    for j in range(1,w+1):
        for k in range(m+1):
            if k + g[i][j]<m:
                dp[i][j][k] = dp[i][j][k] or dp[i-1][j][abs(k-g[i][j])] or dp[i-1][j][k+g[i][j]] or dp[i][j-1][abs(k-g[i][j])] or dp[i][j-1][k+g[i][j]]
            else:
                dp[i][j][k] = dp[i][j][k] or dp[i-1][j][abs(k-g[i][j])] or dp[i][j-1][abs(k-g[i][j])]
            

for k in range(m+1):
    if dp[-1][-1][k]:
        print(k);exit()

