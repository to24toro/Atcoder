h,n = map(int,input().split())
M = []
max_val = 0
for _ in range(n):
    a,b = map(int,input().split())
    max_val = max(max_val,a)
    M.append((a,b))
dp = [float('inf')]*(h+1+max_val)
dp[0] = 0
for i in range(1,h+1+max_val):
    for j in range(n):
            dp[i] = min(dp[i-M[j][0]] + M[j][1],dp[i])
print(min(dp[h:-1]))


