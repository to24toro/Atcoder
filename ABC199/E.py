n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(m)]

dp = [0]*(1<<n)
dp[0] = 1
for b in range(1<<n):
    s = 0
    num = []
    for i in range(n):
        if (b>>i)&1:
            s += 1
        num.append(s)
    f = True
    for i in range(m):
        x,y,z = L[i]
        if x>=s:
            if num[y-1]>z:
                f =False
                break
    if f:
        for i in range(n):
            if (b>>i)&1:
                dp[b] += dp[b&~(1<<i)]
print(dp[-1])
