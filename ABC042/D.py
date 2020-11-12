h,w,a,b =map(int,input().split())
mod = 10**9+7
# dp = [[-1]*w for _ in range(h)]
# dp[0][0]=1
# for i in range(h):
#     dp[i][0]=1
# for j in range(w):
#     dp[0][j]=1
# for i in range(h-a,h):
#     for j in range(b):
#         dp[i][j]=float('inf')
# for i in range(1,h):
#     for j in range(1,w):
#         if dp[i][j]!=float('inf'):
#             if dp[i][j-1]!=float('inf'):
#                 dp[i][j] = dp[i-1][j]+dp[i][j-1]
#                 dp[i][j] %=mod
#             else:
#                 dp[i][j] = dp[i-1][j]
#                 dp[i][j] %=mod
# print(dp[-1][-1])
n = h+w+10
frac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]%mod
finv[-1] = pow(frac[-1],mod-2,mod)
for i in range(1,n+1):
    finv[n-i] = finv[n-i+1]*(n-i+1)%mod
def nCr(n,r):
    if n<0 or r<0 or n<r: return 0
    r = min(r,n-r)
    return frac[n]*finv[n-r]*finv[r]%mod
ans = 0
for j in range(b,w):
    ans += nCr(h-1-a+j,j)*nCr(a-1+w-1-j,a-1)

print(ans%mod)