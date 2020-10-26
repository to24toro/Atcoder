# mod = 10**9+7
# n,m,l = map(int,input().split())
# frac = [1]*(n+1)
# finv = [1]*(n+1)
# for i in range(n):
#     frac[i+1] = (i+1)*frac[i]%mod
# finv[-1] = pow(frac[-1],mod-2,mod)
# for i in range(1,n+1):
#     finv[n-i] = finv[n-i+1]*(n-i+1)%mod
# def nCr(n,r):
#     if n<0 or r<0 or n<r: return 0
#     r = min(r,n-r)
#     return frac[n]*finv[n-r]*finv[r]%mod
# fachalf = [1,1,1,3]
# for i in range(4,n+3):
#     fachalf.append((fachalf[-1]*i)%mod)
# pascal = [[1,0]]
# for i in range(1,n+3):
#     pascal.append([1])
#     for r in range(1,i+1):
#         pascal[-1].append((pascal[-2][r-1] + pascal[-2][r]) % mod)
#     pascal[-1].append(0)
# def helper(s):
#     dp = [[0]*(m+1) for _ in range(n+1)]
#     dp[0][0]=1
#     for i in range(n+1):
#         for j in range(m+1):
#             if dp[i][j]==0: continue
#             for k in range(1,s+1):
#                 if i+k>n or j+k-1>m: break
#                 dp[i+k][j+k-1] = (dp[i+k][j+k-1]+dp[i][j]*pascal[n-i-1][k-1]*fachalf[k])%mod
#             for k in range(2,s+1):
#                 if i+k>n or j+k>m: break
#                 dp[i+k][j+k] = (dp[i+k][j+k]+dp[i][j]*pascal[n-i-1][k-1]*fachalf[k-1])%mod
#     return dp[-1][-1]
# ans = helper(l)-helper(l-1)
# print(ans%mod)
N,M,L = map(int,input().split())
MOD = 10**9+7

pascal = [[1,0]]
for n in range(1,N+3):
    pascal.append([1])
    for r in range(1,n+1):
        pascal[-1].append((pascal[-2][r-1] + pascal[-2][r]) % MOD)
    pascal[-1].append(0)
fachalf = [1,1,1,3]
for i in range(4,N+3):
    fachalf.append((fachalf[-1] * i) % MOD)

def count_maxsize_lessthan_or_equal(s):
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N+1):
        for j in range(M+1):
            if dp[i][j] == 0: continue
            for k in range(1,s+1):
                if i+k > N or j+k-1 > M: break
                dp[i+k][j+k-1] = (dp[i+k][j+k-1] + dp[i][j] * pascal[N-i-1][k-1] %MOD * fachalf[k]) % MOD
            for k in range(2,s+1):
                if i+k > N or j+k > M: break
                dp[i+k][j+k] = (dp[i+k][j+k] + dp[i][j] * pascal[N-i-1][k-1] %MOD * fachalf[k-1]) % MOD
    return dp[-1][-1]

ans = count_maxsize_lessthan_or_equal(L) - count_maxsize_lessthan_or_equal(L-1)
print(ans%MOD)