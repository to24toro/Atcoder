N = int(input())
S = [input().strip() for _ in range(5)]
cL = [[0]*N for _ in range(3)]

for j in range(N):
    r = b = w = 0
    for i in range(5):
        if S[i][j] == 'R':
            r += 1
        elif S[i][j] == 'B':
            b += 1
        elif S[i][j] == 'W':
            w += 1
    cL[0][j] = 5 - r
    cL[1][j] = 5 - b
    cL[2][j] = 5 - w

dp = [[0]*N for _ in range(3)]
for i in range(3):
    dp[i][0] = cL[i][0]

rot = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
for j in range(1, N):
    for k in range(3):
        k0, k1, k2 = rot[k]
        dp[k0][j] = min(dp[k1][j-1], dp[k2][j-1]) + cL[k0][j]

print(min(dp[i][N-1] for i in range(3)))
