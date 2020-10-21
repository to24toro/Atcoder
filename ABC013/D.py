n,d = map(int,input().split())
x,y = map(int,input().split())
if x%d or y%d:print(0);exit()
X = abs(x//d)
Y = abs(y//d)
frac = [1]*(n+1)
for i in range(n):
    frac[i+1] = (i+1)*frac[i]
def helper(n,r):
    if n<0 or r<0 or n<r: return 0
    return frac[n]/(frac[n-r]*frac[r])
if X+Y==n:
    print(pow(0.25,n)*helper(n,X));exit()
if X+Y>n:print(0);exit()
d = n-X-Y
if d%2:
    print(0);exit()
d //=2
ans = 0
for i in range(d+1):
    ans += helper(n,i)*helper(n-i,d-i)*helper(n-d,X+i)*pow(0.25,n)
print(ans);exit()
a,b = map(int,input().split())


def helper(x):
    x = len(str(x))
    dp = [[[0,0],[0,0]] for _ in range(x+1)]
    dp[0][0][0] = 1
    for i in range(x):
        x_i = int(x[i])
        for j in range(x_i):
            if j==4 or j==9:
                dp[i+1][1][1] += dp[i][0][0] + dp[i][0][1]
            else:
                dp[i+1][1][0] += dp[i][0][0]
                dp[i+1][1][1] += dp[i][0][1]
        if x_i ==4 or x_i ==9:
            dp[i+1][0][1] += dp[i][0][0] + dp[i][0][1]
        else:
            dp[i+1][0][0] += dp[i][0][0]
            dp[i+1][0][1] += dp[i][0][1]
        dp[i+1][1][0] += 8 * dp[i][1][0]
        dp[i+1][1][1] += 2 * dp[i][1][0] + 10 * dp[i][1][1]
    return dp[-1][0][1] + dp[-1][1][1]
ans = f(b)-f(a-1)
print(ans)




