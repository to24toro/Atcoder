n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dp=[[10**9 for _ in range(51)] for _ in range(1<<n)]
dp[0][0]=0
for S in range(1<<n):
    j = bin(S).count('1') #何枚選んだか
    c = 0
    for i in range(n):
        if not (S&1<<i):#元々i番目のカードが選ばれていない時、つまりSに含まれていない時
            k = A[i] if (i-j)%2==0 else B[i] #iからj番目に持って来るので
            for l in range(k+1):
                dp[S|1<<i][k] = min(dp[S|1<<i][k],dp[S][l]+c)
            c += 1
ans = min(dp[-1])
print(ans if ans!=10**9 else -1)