s = input()
t = input()
S,T = len(s),len(t)
dp = [[0]*(T+1) for _ in range(S+1)]
for i in range(S):
    for j in range(T):
        if s[i]==t[j]:
            dp[i+1][j+1] = 1 + dp[i][j]
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
ans = ''
i,j = S,T
while dp[i][j]:
    if dp[i][j] ==dp[i][j-1]:
        j-=1
    elif dp[i][j] == dp[i-1][j]:
        i-=1
    else:
        ans = s[i-1] + ans
        i-=1
        j-=1
print(ans)