h,w = map(int,input().split())
A = [[1 if c=="+" else -1 for c in input()] for _ in range(h)]
INF = float('inf')
dp = [[-INF]*w for _ in range(h)]
dp[-1][-1] = 0
for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i+1<h:
            dp[i][j] = max(dp[i][j],A[i+1][j]-dp[i+1][j])
        if j+1<w:
            dp[i][j] = max(dp[i][j],A[i][j+1]-dp[i][j+1])
if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")