h,w = map(int,input().split())
A = [input() for _ in range(h)]
dp = [[float('inf')]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if (i+j)%2:
            dp[i][j] *=-1
for i in range(1,h):
    if A[i][j]=='+':
        dp[i][0]=dp[i-1][0]+(-1)**((i+j)%2)
    else:
        dp[i][0]=dp[i-1][0]-(-1)**((i+j)%2)
for i in range(1,w):
    if A[i][j]=='+':
        dp[0][i]=dp[0][0]+(-1)**((i+j)%2)
    else:
        dp[0][i]=dp[i-1][0]-(-1)**((i+j)%2)
dp[0][0] = 0
for i in range(1,h):
    for j in range(1,w):
        if (i+j)%2:
            if i+1<h and  A[i+1][j]=='+':
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]-1)
            elif i+1<h and  A[i+1][j]=='-':
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1)
            if j+1<w and  A[i][j+1]=='+':
                dp[i][j+1] = min(dp[i][j+1],dp[i][j]-1)
            elif j+1<w and A[i][j+1]=='-':
                dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
        else:
            if i+1<h and  A[i+1][j]=='+':
                dp[i+1][j] = max(dp[i+1][j],dp[i][j]+1)
            elif i+1<h and  A[i+1][j]=='-':
                dp[i+1][j] = max(dp[i+1][j],dp[i][j]-1)
            if j+1<w and A[i][j+1]=='+':
                dp[i][j+1] = max(dp[i][j+1],dp[i][j]+1)
            elif j+1<w and A[i][j+1]=='-':
                dp[i][j+1] = max(dp[i][j+1],dp[i][j]-1)

if dp[-1][-1]>0:
    print('Takahashi')
elif dp[-1][-1]==0:
    print('Draw')
else:
    print('Aoki')




