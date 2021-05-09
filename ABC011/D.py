n,d = map(int,input().split())
x,y = map(int,input().split())


if x%d==0  and y%d==0:
    x=x//d
    y=y//d
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        if i==0:
            dp[i][0] = dp[i][i]=1
        else:
            dp[i][0]=dp[i][i]=dp[i-1][0]/2
        for j in range(1,i):
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])/2
 
    ans=0
    for i in range(n+1):
        rest=n-i
        x=abs(x)
        y=abs(y)
        if i>=x and (i+x)%2==0 and rest>=y and (rest+y)%2==0:
 
            ans+=dp[i][(i+x)//2]*dp[rest][(rest+y)//2]*dp[n][i]
            
 
    print(ans)
 
else:
    print(0)