S = input()
T = input()
s = len(S)
t = len(T)
dp = [[0]*(t) for _ in range(s)]

f = False
for i in range(s):
    if T[0]==S[i] or f:
        dp[i][0] = 1
        f = True
f = False
for j in range(t):
    if S[0]==T[j] or f:
        dp[0][j] = 1
        f = True

for i in range(1,s):
    for j in range(1,t):
        if S[i]==T[j]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])
