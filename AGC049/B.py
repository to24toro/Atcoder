n = int(input())
S = input()
S  =S[::-1]
T = input()[::-1]
dp = [[0,0] for _ in range(n)]
if S[0]=='0' and S[0]!=T[0]:
    print(-1);exit()

for i in range(n-1):
    if T[i]=='0':
        if S[i]=='0':
            if S[i+1]=='0':
                dp[i+1][0]=dp[i][0]
            else:
                dp[i+1][1]= dp[i][0]
        else:
            if S[i+1]!=T[i+1]:
                dp[i+1][T[i+1]] = 1 + dp[i][1]
            else:
                if S[i+1]=='0':
                    dp[i+1][0] = 1+dp[i][1]
                else:
                    dp[i+1][1] = 1+dp[i][0]
    else:
        if S[i]=='1':
            if S[i+1]=='0':
                dp[i+1][0]=dp[i][1]
            else:
                dp[i+1][1] = dp[i][1]
        else:
            continue
print(min(dp[-1]))

