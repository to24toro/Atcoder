n = int(input())
s = input()
mod = 10007
ans = 0
dp = [[0]*(n+1) for _ in range(8)]
dp[1][0] = 1
for i in range(n):
    if s[i] =='J':
        j = 0
    elif s[i] =='O':
        j = 1
    else:
        j = 2
    for now in range(8):
        for nxt in range(8):
            if (nxt>>j)&1 and (now&nxt):
                dp[nxt][i+1] += dp[now][i]
                dp[nxt][i+1] %=mod
for i in range(8):
    ans += dp[i][-1]
print(ans%mod)

