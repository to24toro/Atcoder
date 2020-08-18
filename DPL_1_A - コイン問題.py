n,m = map(int,input().split())
C = list(map(int,input().split()))
dp = [float('inf') for _ in range(n+1)]
for c in C:
    if c<=n:
        dp[c] =1
for i in range(n+1):
    for c in C:
        if i-c >0:
            dp[i] = min(dp[i],dp[i-c] + 1)
# print(dp)
print(dp[-1])