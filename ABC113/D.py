h,w,K = map(int,input().split())
mod = 10**9+7
dp = [[0]*(w) for _ in range(h+1)]
dp[0][0] = 1
K-=1
for i in range(h):
    for j in range(w):
        for bit in range(1<<(w-1)):
            f = True
            for k in range(w-2):
                if (bit&(1<<k)) and (bit&(1<<(k+1))):
                    f = False
            if not f: continue
            l = j
            if bit&(1<<j):l+=1
            elif (j>0 and (bit&(1<<(j-1)))):l-=1
            dp[i+1][l] += dp[i][j]
            dp[i+1][l] %=mod
print(dp[h][K]%mod)
