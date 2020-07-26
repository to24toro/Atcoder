n = int(input())
A = list(map(int,input().split()))
one = A.count(1)
two = A.count(2)
three = A.count(3)

dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
for sushi in range(1,n+1):
    for k in range(sushi+1):
        for j in range(sushi-k+1):
            i = sushi-k-j
            if i != 0:
                dp[i][j][k] += dp[i - 1][j][k] * i / sushi
            if j != 0:
                dp[i][j][k] += dp[i + 1][j - 1][k] * j / sushi
            if k != 0:
                dp[i][j][k] += dp[i][j + 1][k - 1] * k / sushi
            dp[i][j][k] += n / sushi
print(dp[one][two][three])