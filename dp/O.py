n,k = map(int,input().split())
A = list(map(int,input().split()))
dp = [False]*(k+1)
for i in range(k+1):
    for a in A:
        if i + a<k+1:
            dp[i+a] |= not dp[i]
        else:
            break
print('First' if dp[k] else 'Second')