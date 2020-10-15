W = int(input())
N,K = map(int,input().split())
dp = [[0 for _ in range(W + 1)] for _ in range(K + 1)]
 
for n in range(1, N + 1):
    a, b = map(int, input().split())
    for k in reversed(range(K+1)):
        for w in range(W+1):
            if k>=1 and w>=a:
                dp[k][w] = max(dp[k][w], dp[k-1][w-a]+b)
ans = dp[K][W]
print(ans)