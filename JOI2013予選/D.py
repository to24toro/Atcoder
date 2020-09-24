d,n = map(int,input().split())
T = [ int(input()) for _ in range(d)]
N = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(d)]

for i in range(1,d):
    for j in range(n):
        for m in range(n):
            if i==1 and not (N[m][0]<=T[0] and T[0]<=N[m][1]):
                continue
            if N[j][0]<=T[i] and T[i]<=N[j][1]:
                dp[i][j] = max(dp[i][j],dp[i-1][m] + abs(N[j][2]-N[m][2]))
print(max(dp[-1]))

