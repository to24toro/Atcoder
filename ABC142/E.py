n,m = map(int,input().split())
P = [[0,0]]
ans = float('inf')
for _ in range(m):
    a,b = map(int,input().split())
    t =[(str(0))]*n
    c = list(map(int,input().split()))
    for i in range(b):
        t[c[i]-1]= str(1)
    P.append([a,''.join(t)])
# print(P)
dp = [[float('inf')]*(1<<n) for _ in range(m+1)]
dp[0][0] = 0
for i in range(1,m+1):
    x= int(P[i][1],2)
    for bit in range(1<<n):
        dp[i][bit] = min(dp[i][bit],dp[i-1][bit])
        dp[i][x|bit]= min(dp[i-1][x|bit],dp[i-1][bit]+P[i][0],dp[i][x|bit])

print(dp[-1][-1] if dp[-1][-1] != float('inf') else -1)
