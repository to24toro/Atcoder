h,w,k = map(int,input().split())
S = [["."]*w for _ in range(h)]
for _ in range(k):
    a,b,c = map(str,input().split())
    a = int(a)-1
    b = int(b)-1
    S[a][b]=c

dp = [0]*w
mod = 998244353
dp[0] = 1
for i in range(1,w):
    if S[0][i]=='.':
        dp[i] = 2*dp[i-1]
    elif S[0][i]!='D':
        dp[i] = dp[i-1]
    else:
        dp[i] = 0

for i in range(1,h):
    dp2 = dp
    for j in range(w):
        if j ==0:
            if S[i-1][0]=='R':
                dp2[0]= 0
            elif S[i-1][0]=='.':
                
            else:
                dp2[0]= 0
        else:
            if S[i][j-1] == 'D':
                if S[i-1][j] == 'R':
                    dp2[j] = 0
                else:
                    continue
            else:
                if S[i-1][j] == 'R':
                    dp2[j] = dp2[j-1]
                else:
                    dp2[j] += dp[j-1]
                    dp2[j]%=mod
    print(dp2)
    dp = dp2
print(dp[-1]%mod)


